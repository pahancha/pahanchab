import os
import re
import yaml
from datetime import datetime

def extract_date_from_filename(filename):
    # Extract date from Jekyll filename format (YYYY-MM-DD-title.md)
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', filename)
    if match:
        year, month, day = match.groups()
        # Return formatted date for Hugo
        return f"{year}-{month}-{day}T00:00:00+05:30"
    return None

def convert_front_matter(jekyll_content, post_date):
    # Extract Jekyll front matter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', jekyll_content, re.DOTALL)
    if not match:
        return None, None
    
    front_matter_yaml = match.group(1)
    content = match.group(2)
    
    # Parse YAML front matter
    jekyll_fm = yaml.safe_load(front_matter_yaml)
    
    # Create Hugo front matter string directly
    hugo_front_matter = '+++\n'
    hugo_front_matter += f"title = '{jekyll_fm.get('title', '')}'\n"
    hugo_front_matter += f"date = {post_date}\n"
    hugo_front_matter += "draft = false\n"
    
    # Convert tags
    if 'tags' in jekyll_fm:
        tags_str = str(jekyll_fm['tags']).replace('[', '').replace(']', '')
        hugo_front_matter += f"tags = [{tags_str}]\n"
    
    hugo_front_matter += '+++\n'
    
    return hugo_front_matter, content

def convert_post(input_file, output_dir):
    # Get the original filename without changing it
    original_filename = os.path.basename(input_file)
    post_date = extract_date_from_filename(original_filename)
    if not post_date:
        print(f"Could not extract date from {original_filename}")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert front matter and get content
    hugo_front_matter, post_content = convert_front_matter(content, post_date)
    if not hugo_front_matter:
        print(f"Failed to process {input_file}")
        return
    
    # Use the exact same filename as Jekyll
    output_path = os.path.join(output_dir, original_filename)
    
    # Write converted post
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(hugo_front_matter)
        f.write(post_content)
    
    print(f"Converted {input_file} -> {output_path}")

def main():
    # Configure these paths
    jekyll_posts_dir = '/Users/pahancha/Documents/blog/pahancha.github.io/_posts'  # Your Jekyll posts directory
    hugo_posts_dir = '/Users/pahancha/Documents/Projects/pahanchab/pahanchab/pahancha-blog/content/posts'  # Your Hugo posts directory
    
    # Create Hugo posts directory if it doesn't exist
    os.makedirs(hugo_posts_dir, exist_ok=True)
    
    # Convert all posts
    for filename in os.listdir(jekyll_posts_dir):
        if filename.endswith('.md') or filename.endswith('.markdown'):
            input_path = os.path.join(jekyll_posts_dir, filename)
            convert_post(input_path, hugo_posts_dir)

if __name__ == '__main__':
    main()