import re

log_path = r'C:\Users\Danial Saleem\.gemini\antigravity\brain\586f0cda-7af8-4e1c-afc5-738880b56fba\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the text block that looks like styles.css and extract the whole block
# We can find where the CSS starts and ends.
starts = [m.start() for m in re.finditer(r':root\s*{', content)]
for s in starts:
    # Get 100 characters before and 500 characters after
    print("--- MATCH ---")
    print(content[max(0, s-100):s+500])
    
