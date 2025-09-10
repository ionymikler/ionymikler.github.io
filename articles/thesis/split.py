#!/usr/bin/env python3
"""
HTML Article Splitter for Early Exit Networks Article
Splits the large HTML file into separate sections based on h1 headers
"""

import re
from pathlib import Path

def extract_css_and_head(html_content):
    """Extract the CSS styles and head section for reuse in all files"""
    head_match = re.search(r'<head>(.*?)</head>', html_content, re.DOTALL)
    if head_match:
        return head_match.group(1)
    return ""

def create_html_template(head_content, title, body_content):
    """Create a complete HTML document with the given content"""
    return f"""<html>
<head>
{head_content}
    <title>{title}</title>
</head>
<body>
    <article class="page sans">
        <header>
            <h1 class="page-title">{title}</h1>
        </header>
        <div class="page-body">
{body_content}
        </div>
    </article>
</body>
</html>"""

def split_html_article(html_content):
    """Split the HTML article into sections based on h1 headers"""
    
    # Extract head content for reuse
    head_content = extract_css_and_head(html_content)
    
    # Extract the main content between <div class="page-body"> and </div>
    body_match = re.search(r'<div class="page-body">(.*?)</div>\s*</article>', html_content, re.DOTALL)
    if not body_match:
        print("Could not find page-body content")
        return {}
    
    main_content = body_match.group(1)
    
    # Find all h1 headers and split content
    h1_pattern = r'<h1[^>]*>(.*?)</h1>'
    h1_matches = list(re.finditer(h1_pattern, main_content, re.DOTALL))
    
    sections = {}
    
    # Handle content before first h1 (introduction)
    if h1_matches:
        intro_content = main_content[:h1_matches[0].start()]
        if intro_content.strip():
            sections['00_introduction'] = {
                'title': 'Introduction and Overview',
                'content': intro_content
            }
    
    # Process each h1 section
    for i, match in enumerate(h1_matches):
        # Clean up the title for filename
        title = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        title = re.sub(r'[^\w\s-]', '', title)  # Remove special chars
        title = re.sub(r'\s+', '_', title)  # Replace spaces with underscores
        
        # Get content from this h1 to the next h1 (or end)
        start_pos = match.start()
        if i + 1 < len(h1_matches):
            end_pos = h1_matches[i + 1].start()
            content = main_content[start_pos:end_pos]
        else:
            content = main_content[start_pos:]
        
        # Create filename with number prefix for ordering
        filename = f"{i+1:02d}_{title.lower()}"
        
        sections[filename] = {
            'title': re.sub(r'<[^>]+>', '', match.group(1)).strip(),
            'content': content
        }
    
    return sections, head_content

def save_sections(sections, head_content, output_dir="article_sections"):
    """Save each section as a separate HTML file"""
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    saved_files = []
    
    for filename, section_data in sections.items():
        file_path = output_path / f"{filename}.html"
        
        html_content = create_html_template(
            head_content,
            section_data['title'],
            section_data['content']
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        saved_files.append(str(file_path))
        print(f"Created: {file_path}")
    
    return saved_files

def create_index_file(sections, head_content, output_dir="article_sections"):
    """Create an index file with links to all sections"""
    
    index_content = """
    <h2>Article Sections</h2>
    <nav>
        <ul>
    """
    
    for filename, section_data in sections.items():
        index_content += f'        <li><a href="{filename}.html">{section_data["title"]}</a></li>\n'
    
    index_content += """
        </ul>
    </nav>
    
    <h2>Original Article</h2>
    <p>This article discusses Early Exit Networks for Computer Vision, focusing on the LGViT model and implementation challenges for production environments.</p>
    """
    
    index_html = create_html_template(
        head_content,
        "Early Exit Networks for Computer Vision - Article Index",
        index_content
    )
    
    index_path = Path(output_dir) / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"Created index: {index_path}")
    return str(index_path)

# Example usage
def main():
    # Read the HTML file
    with open('ee-in-cv-pt1.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Split into sections
    sections, head_content = split_html_article(html_content)
    
    # Save sections
    saved_files = save_sections(sections, head_content)
    
    # Create index
    index_file = create_index_file(sections, head_content)
    
    print(f"\nSplit complete! Created {len(saved_files)} section files plus index.")
    print(f"All files saved in 'article_sections/' directory")
    
    return saved_files + [index_file]

if __name__ == "__main__":
    main()