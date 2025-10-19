# Comprehensive Guide to Protective Licensing for Skills

## Why Protective Licensing Matters

Custom skills represent valuable intellectual property that requires protection from:
- Unauthorized AI/ML training use
- Commercial exploitation without permission
- Redistribution without attribution
- Modification without authorization

## The Protective Skills License

The Protective Skills License v1.0 provides comprehensive protection through:

### 1. Explicit AI/ML Training Prohibition

The license explicitly forbids use of skill content for:
- Training any artificial intelligence or machine learning system
- Fine-tuning, pre-training, or post-training of models
- Creating embeddings or vector representations
- Building retrieval-augmented generation (RAG) systems
- Data mining or scraping for AI purposes
- Generating synthetic data from skill content

### 2. Copyright Establishment

Clear copyright ownership for:
- Individual developers
- Corporations (including medical corporations)
- Limited Liability Companies (LLCs)
- Joint entity ownership structures

### 3. Commercial Use Controls

Requires explicit written permission for:
- Commercial use of skills
- Selling or licensing skills
- Including skills in commercial products
- Redistributing through marketplaces

## Implementation Strategy

### For New Skills

When creating a new skill:

1. Initialize the skill using skill-creator
2. Apply protective license immediately:
   ```bash
   python apply_license.py --skill-path ./my-skill \
     --entity-name "My Company" \
     --entity-type corporation \
     --jurisdiction "Delaware"
   ```
3. Validate the application:
   ```bash
   python validate_licensing.py --skill-path ./my-skill
   ```

### For Existing Skills

To protect existing skills:

1. Back up your skill directory
2. Apply the license:
   ```bash
   python update_skill_license.py --skill-path ./existing-skill \
     --entity-name "My Name" \
     --backup true
   ```
3. Review and commit changes

## Entity Structure Options

### Individual Developer

For personal projects:
- Entity type: `individual`
- Jurisdiction: Your state/country of residence
- Copyright: Personal name

### Single Corporation

For company-owned skills:
- Entity type: `corporation`
- Jurisdiction: State of incorporation
- Copyright: Company legal name

### Joint Ownership

For skills owned by multiple entities:
- Primary entity: Operating company
- Secondary entity: Holding company or partner
- Jurisdiction: Primary entity's location
- Copyright: Both entities listed

Example:
```
Copyright (c) 2025 OperatingCo, Inc. and HoldingCo, LLC
```

## Platform-Specific Considerations

### Anthropic Claude

For skills used with Claude:
- Consumer accounts: Must opt out of training via Settings > Privacy
- API/Commercial accounts: Protected by commercial terms (no training by default)
- Skills uploaded: Subject to account type terms

### Other AI Platforms

The license prohibits training use regardless of platform:
- OpenAI / ChatGPT
- Google Gemini
- Microsoft Copilot
- Open source models
- Any other AI/ML system

## Enforcement Mechanisms

### License Violations

The license provides for:
1. Immediate termination of granted licenses
2. Legal action for copyright infringement
3. Injunctive relief to stop violations
4. Recovery of attorneys' fees and costs

### Monitoring

To monitor for violations:
- Regularly search for your skill content online
- Use plagiarism detection tools
- Monitor AI model outputs for your content
- Document any suspected violations

## Best Practices

### Documentation

Always maintain:
- Original creation dates
- Development history
- Entity ownership records
- License application logs

### Version Control

For skills in git repositories:
1. Commit LICENSE.txt with initial skill
2. Include license reference in README
3. Tag releases with license version
4. Maintain license history

### Communication

When sharing skills:
- Always include LICENSE.txt
- Reference license in documentation
- Clarify permitted uses upfront
- Provide clear contact information

## FAQ

### Q: Can I change the license later?
A: Yes, but only for new versions. Previously distributed versions remain under their original license.

### Q: What about open source contributions?
A: The protective license is incompatible with most open source licenses. Consider dual licensing if needed.

### Q: How do I allow specific uses?
A: Grant written permission on a case-by-case basis, documenting each permission granted.

### Q: What about educational use?
A: Personal educational use is permitted, but institutional training programs require permission.

### Q: Can I sell skills with this license?
A: Yes, you retain commercial rights. Buyers receive usage rights but cannot redistribute or train AI on the content.

## Legal Considerations

**Disclaimer**: This guide provides general information only. Consult with a qualified attorney for specific legal advice regarding:
- Jurisdiction-specific requirements
- International copyright law
- Enforcement strategies
- License customization needs

## Contact Information

For questions about the Protective Skills License or this guide:
- Review the license template in `PROTECTIVE-SKILLS-LICENSE-TEMPLATE.txt`
- Consult the validation script documentation
- Seek legal counsel for specific situations