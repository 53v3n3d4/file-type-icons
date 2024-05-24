CONTEXTS_MAIN = {'contexts': {'main': []}}

# Scopes used in 'contexts', sublime-syntax files. In case, syntax not installed
# or disable, this needs to be removed. Or user receive an error
# message in console about syntax not found.
CONTEXTS_SCOPES = [
    {'scope': 'source.ini', 'startsWith': 'INI ('},
    {'scope': 'source.js', 'startsWith': 'JavaScript ('},
    {'scope': 'source.json', 'startsWith': 'JSON ('},
    {'scope': 'source.jsx', 'startsWith': 'JSX ('},
    {'scope': 'source.makefile', 'startsWith': 'Makefile ('},
    {'scope': 'source.python', 'startsWith': 'Python ('},
    {'scope': 'source.ruby', 'startsWith': 'Ruby ('},
    {'scope': 'source.shell', 'startsWith': 'Shell ('},
    {'scope': 'source.toml', 'startsWith': 'TOML ('},
    {'scope': 'source.ts', 'startsWith': 'TypeScript ('},
    {'scope': 'source.tsx', 'startsWith': 'TSX ('},
    {'scope': 'source.webidl', 'startsWith': 'IDL ('},
    {'scope': 'source.yaml', 'startsWith': 'YAML ('},
    {'scope': 'text.bibtex', 'startsWith': 'BibTex ('},
    {'scope': 'text.git.ignore', 'startsWith': 'Git ('},
    {'scope': 'text.html.basic', 'startsWith': 'HTML ('},
    {'scope': 'text.html.markdown', 'startsWith': 'Markdown ('},
    # {'scope': 'text.plain', 'startsWith': 'Plain Text ('},
    {'scope': 'text.xml', 'startsWith': 'XML ('},
    # Custmos
    {'scope': 'source.js', 'startsWith': 'UnitTest (JavaScript)'},
    {'scope': 'source.jsx', 'startsWith': 'UnitTest (JSX)'},
    {'scope': 'source.tsx', 'startsWith': 'UnitTest (TSX)'},
    {'scope': 'source.ts', 'startsWith': 'UnitTest (TypeScript)'},
    {'scope': 'text.html.basic', 'startsWith': 'XML (SVG)'},
]