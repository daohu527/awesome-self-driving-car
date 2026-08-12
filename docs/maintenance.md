# Maintenance Guide

## Purpose
This repository should stay useful as a curated map of the autonomous-driving field, not just a growing list of URLs.

The value of the project comes from its structure, not just its size. If the taxonomy is strong, both humans and AI systems can navigate the material quickly and correctly.

## High-priority content to maintain
These are the categories that matter most for the repository's usefulness:

1. Technology stack overview
   - The core stack diagram and the conceptual explanation of how the system is organized.

2. Open-source fullstack systems
   - Apollo, Autoware, openpilot, and similar foundational references.

3. Core surveys and canonical papers
   - Survey papers are the best onboarding path for perception, localization, planning, and control.

4. Courses and learning paths
   - Good onboarding resources help readers understand the vocabulary before deep dives.

5. Domain-specific references
   - Important breakthroughs should be organized by their actual engineering domain.

6. Hardware and systems context
   - Sensors, cloud services, RTOS, deployment, and integration layers matter for real-world understanding.

These sections should be reviewed more carefully than the long tail of less important links.

## Editorial policy
When adding or editing entries:

- Place each entry in the correct domain.
- Keep the list stable and readable.
- Prefer a short description over a vague recommendation.
- Avoid duplicate or near-duplicate references.
- Keep older but historically important items labeled as historical if needed.

## AI-friendly metadata model
For future extensibility, each item should eventually follow a small metadata schema such as:

```yaml
- title: "Apollo"
  type: "opensource"
  domain: "fullstack"
  year: 2024
  url: "https://apollo.auto/"
  summary: "Open-source autonomous driving platform."
  tags: ["fullstack", "planning", "perception"]
```

This format is lightweight, human-readable, and easy for an AI agent to parse. The repository now includes a structured catalog at `catalog/primary-references.yaml` as the first step toward this metadata approach.

## AI role in maintenance
AI can help with the following tasks:

- Detect duplicates and stale links
- Suggest missing category labels
- Summarize a paper or project in one sentence
- Find new relevant references within a domain
- Rank references by importance for a given topic

However, AI should not be the sole source of editorial quality. Human judgment is still needed to decide: what is foundational, what is secondary, and what is noise.

## Recommended workflow
1. Update the README when the overall taxonomy changes.
2. Update the AI guide when the conceptual stack or reading flow changes.
3. Add or refine entries in the relevant domain section.
4. Review links and metadata regularly.
5. Keep the repository scoped to the most important knowledge, not every possible reference.

## Summary
This project remains useful when it stays curated, categorized, and interpretable. AI can accelerate maintenance, but the repository still needs a strong editorial backbone to remain a trustworthy knowledge base.
