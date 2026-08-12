# AI Reading Guide for the Autonomous Driving Knowledge Base

## Project identity
This repository is not a runnable software project. It is a curated knowledge repository for autonomous driving research and systems. The goal is to connect a broad set of references into a structured map that is useful for both humans and AI agents.

The repository organizes knowledge around the standard autonomous-driving pipeline:

- Sensors and hardware
- Localization and mapping
- Perception
- Prediction
- Planning
- Control
- Simulation and validation
- Cloud, systems, and deployment

## Why this repo is AI-friendly
AI systems benefit from clear conceptual boundaries. This repository makes those boundaries explicit through the taxonomy in the README and the domain sections. Each major section has a concrete purpose:

- Open-source projects show available implementations.
- Courses provide learning curve and onboarding paths.
- Papers and blogs explain techniques and their evolution.
- Datasets and benchmarks provide evaluation ground truth.
- Algorithms connect methods to concrete tasks.
- Systems and hardware explain deployment realities.

This structure helps an agent decide whether it needs a practical implementation, a theoretical reference, or a system-level perspective.

## Recommended reading flow
For a new reader or AI agent, a practical order is:

1. Read the technology stack diagram and the overview sections.
2. Study the course list to establish the common vocabulary.
3. Check the open-source fullstack projects to understand real system architecture.
4. Move to specific domains such as perception, localization, planning, and control.
5. Use survey papers to understand the problem and then dive into a specific paper or implementation.
6. End with datasets, algorithms, and system/hardware references for evaluation and deployment.

## Domain map
### 1. Sensor and hardware layer
This includes cameras, LiDAR, radar, GPS/IMU, CAN, drive-by-wire, black-box systems, and HMI devices. These components define the raw observability and controllability of the vehicle.

### 2. Localization and mapping
This includes GPS/IMU fusion, SLAM, HD map creation, calibration, and map matching. Without accurate localization, the downstream planning stack cannot be reliable.

### 3. Perception
A central domain that includes object detection, 3D object detection, tracking, lane detection, semantic segmentation, and multi-sensor fusion. Perception is the interpretation of the environment from raw sensor data.

### 4. Prediction
Prediction estimates how agents (cars, pedestrians, cyclists) will behave. It bridges perception and planning by turning recognized objects into future trajectories or intent probabilities.

### 5. Planning
Planning decides what action the vehicle should take next. This category includes route planning, behavior planning, and motion planning under constraints such as safety, comfort, and traffic rules.

### 6. Control
Control converts planning decisions into actuator commands. It includes longitudinal and lateral control, path tracking, and vehicle dynamics modeling.

### 7. Simulation and validation
This layer includes scenario generation, synthetic data, digital twins, and benchmark evaluation. It is critical for testing before real-world deployment.

### 8. System and cloud infrastructure
This covers ROS, middleware, RTOS, monitoring, OTA, cloud simulation, map services, and data ingestion infrastructure. These systems support deployment at scale.

## Core idea behind the stack
The stack should be read as a pipeline of increasing abstraction:

- Sensors capture raw signals.
- Localization and maps anchor the ego vehicle in the world.
- Perception extracts semantic objects and scene information.
- Prediction estimates future motion.
- Planning chooses safe behavior.
- Control realizes the decision in vehicle dynamics.
- Simulation and data services validate the full system.

A good autonomous-driving understanding comes from seeing how each layer depends on the previous one.

## Practical guidance for AI agents
When using this repository, prefer the following workflow:

- If the task is implementation-oriented, search the open-source fullstack and library sections first.
- If the task is academic, start with survey papers and then move to concrete papers in the relevant subdomain.
- If the task is system design, inspect hardware, cloud service, and RTOS references after understanding the software stack.
- If the task concerns safety or validation, focus on simulation, benchmark, and planning/control literature.

## Maintenance guidance for long-term quality
If this repository continues to grow, keep it AI-friendly by following a few simple rules:

1. Maintain a stable taxonomy.
   - Keep the top hierarchy stable: open-source, courses, papers, datasets, algorithms, systems, hardware, big players.
   - Do not create ad hoc categories without reflecting them in the README table of contents.

2. Standardize each entry.
   - For each item, prefer a consistent shape: name, URL, short description, domain, year, type, and tags.
   - This makes it easier for both humans and AI systems to filter and compare references.

3. Prefer canonical domains over free-form labels.
   - Use labels like perception, localization, prediction, planning, control, simulation, and hardware.
   - Avoid mixing too many one-off tags such as "interesting" or "good read".

4. Keep links healthy.
   - Periodically validate URLs and remove stale entries.
   - Mark outdated items with a clear status note if they are historically important but no longer active.

5. Keep the README as the index, not the full database.
   - The README should stay navigable and short.
   - Detailed raw entries can be organized into internal docs or structured metadata files later.

6. Add lightweight metadata for AI use.
   - A future improvement would be YAML or JSON metadata with fields like `title`, `category`, `domain`, `year`, `type`, `url`, `summary`, `tags`.
   - This would let an LLM or script rank, classify, and summarize references automatically.

## What really matters to maintain
AI can fetch or update references, but it cannot replace a curated source of meaning without a human-designed taxonomy and editorial judgment.

The repository's most important content is therefore not the raw size of the list, but the quality of its organizing logic:

- The stack view: what belongs to perception, localization, planning, control, and so on
- The curated entry points: courses, fullstack systems, and classic surveys
- The domain routing: which references are primary, secondary, or historical
- The maintenance policy: how new material is judged and classified

This is where human curation remains valuable. AI can help with automation, but the repository still needs a clear state-of-the-art map to avoid becoming noisy or redundant.

## Suggested future evolution
To make this project even more AI-friendly, a useful next step is to split the current single list into:

- `README.md`: human landing page and summary
- `docs/ai-reading-guide.md`: conceptual map and reading workflow
- `docs/maintenance.md`: contribution and curation policy
- `data/` or `catalog/`: structured metadata files for references

This keeps the repository easy for humans to browse while giving AI systems a clean, structured source of truth.

## Summary
This repository is best understood as a curated map of the autonomous-driving field. It is intentionally broad and interdisciplinary. For AI reading, the most productive approach is to follow the stack, identify the current layer of interest, and then drill into the most relevant references rather than reading the whole repository linearly.
