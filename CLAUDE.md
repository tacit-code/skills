# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Anthropic Skills repository, containing example and reference implementations of Agent Skills. Skills are modular, self-contained packages that dynamically extend Claude's capabilities for specialized tasks through instructions, scripts, and bundled resources.

The repository consists of:
- **Example Skills** (Apache 2.0): Open source skills demonstrating various patterns
- **Document Skills** (Proprietary): Reference implementations of production document processing skills (source-available for learning)
- **Template & Meta Skills**: Tools for creating new skills

## Architecture

### Skill Structure Pattern

Every skill follows the Agent Skills Specification (see agent_skills_spec.md:1):

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description, optional: license, allowed-tools, metadata)
│   └── Markdown instructions
└── Optional subdirectories:
    ├── scripts/     - Python/Bash/JS executables for deterministic operations
    ├── templates/   - Reusable templates (p5.js generators, document templates)
    ├── reference/   - Documentation loaded on-demand
    ├── examples/    - Example outputs or usage demonstrations
    └── core/        - Shared libraries (e.g., GIF generation)
```

### Plugin Distribution System

Skills are distributed via Claude Code Plugin marketplace (see .claude-plugin/marketplace.json:1):
- **document-skills plugin**: docx, xlsx, pptx, pdf
- **example-skills plugin**: All other example skills

Skills can be installed via:
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

### Skill Categories

**Document Skills** (document-skills/):
- Complex production implementations working with binary formats
- Heavy use of Python/Node.js scripts for deterministic operations
- OOXML manipulation (docx/pptx share ooxml/ subdirectory)
- Key scripts: unpack.py, pack.py, validate.py

**Creative/Design Skills**:
- algorithmic-art: p5.js generative art with templates/
- canvas-design: Visual design with embedded fonts
- slack-gif-creator: Python-based GIF generation with core/ library

**Development Skills**:
- mcp-builder: MCP server creation with evaluation scripts
- artifacts-builder: HTML artifact creation with scripts/
- webapp-testing: Playwright-based testing with scripts/

**Meta Skills**:
- skill-creator: Skill development guidance with utility scripts (init_skill.py, package_skill.py, quick_validate.py)
- template-skill: Minimal starting template

## Development Guidelines

### Working with Skills

**Testing a Skill**:
Skills are loaded dynamically by Claude. To test locally in Claude Code:
1. Reference the skill directory in conversation
2. Ask Claude to use a specific skill by name
3. Verify YAML frontmatter matches agent_skills_spec.md requirements

**Creating New Skills**:
Use skill-creator skill or reference template-skill/:
- Frontmatter requires `name` (hyphen-case, matches directory) and `description` (when to use it)
- Description quality determines activation - be specific about use cases
- Use third-person for descriptions ("This skill should be used when...")

**Scripts Best Practices**:
- Use scripts/ for operations requiring deterministic reliability
- Python is preferred for document manipulation
- JavaScript for p5.js/browser-based operations
- All scripts should be executable and include appropriate shebangs

### OOXML Document Skills Architecture

The docx and pptx skills share OOXML manipulation utilities:
- `ooxml/scripts/unpack.py` - Extract .docx/.pptx to XML
- `ooxml/scripts/pack.py` - Repackage XML back to Office format
- `ooxml/scripts/validate.py` - Validation framework
- `ooxml/scripts/validation/` - Format-specific validators

**Workflow Pattern**:
```bash
# 1. Unpack Office file to XML
python ooxml/scripts/unpack.py input.docx output_dir/

# 2. Edit XML in output_dir/

# 3. Validate changes
python ooxml/scripts/validate.py output_dir/

# 4. Repack to Office format
python ooxml/scripts/pack.py output_dir/ output.docx
```

### Document Skills Conversion Tools

**Pandoc Integration** (docx, xlsx):
- Text extraction: `pandoc --track-changes=all input.docx -o output.md`
- Preserves structure and tracked changes
- Used for read-only content analysis

**HTML to PPTX** (pptx/scripts/html2pptx.js:1):
- Node.js script for converting HTML to PowerPoint
- Handles complex layouts and templates

### Common Dependencies

**Python** (document-skills, slack-gif-creator, mcp-builder, skill-creator):
- Check requirements.txt in skill directories
- Key libraries: python-docx, openpyxl, python-pptx, PyPDF2, Pillow

**Node.js** (algorithmic-art, pptx):
- p5.js for generative art
- html2pptx conversion pipeline

**Playwright** (webapp-testing):
- Browser automation for testing local web apps

## Key Files Reference

- `README.md:1` - Repository introduction and usage guide
- `agent_skills_spec.md:1` - Official specification (v1.0)
- `.claude-plugin/marketplace.json:1` - Plugin distribution configuration
- `template-skill/SKILL.md:1` - Minimal skill template
- `skill-creator/SKILL.md:1` - Comprehensive skill development guide

## Important Notes

- Document skills are **point-in-time snapshots** and not actively maintained in this repo
- Production versions ship with Claude and may differ from these references
- Skills are primarily for demonstration and learning
- Always test skills thoroughly before production use
- SKILL.md name field must match directory name exactly
