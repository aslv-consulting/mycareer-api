# My Career Documentation

## Project structure

    mycareer
    |-- docs             # Generated documentation files for github pages
    |-- mkdocs           # MkDocs configuration and related files
    |-- mycareer         # Main application source code
        | -- __init__.py # Package initialization file
        | -- main.py     # Main application entry point
        | -- models.py   # Data models and schemas
    |-- requirements     # Dependency requirements files
    |-- tests            # Unit and integration tests

## Tests coverage

The coverage is available [here](coverage/index.html)

## Goals Features

**Career Planning**: Enable users to plan their career paths by setting short-term and long-term goals.

- **Goal Setting**: Allow users to set and manage career goals.
- **Milestone Tracking**: Enable users to track progress towards their goals with milestones.
- **Career Path Visualization**: Provide visual tools to map out potential career paths.

**Skill Development**: Provide tools and resources for users to identify and develop necessary skills for their career advancement.

- **Skill Assessment**: Offer assessments to help users identify skill gaps.
- **Learning Resources**: Integrate with platforms like Coursera, Udemy, etc., to recommend courses.
- **Progress Tracking**: Track the completion of courses and skill development activities.

**Job Search**: Facilitate job searching by integrating job listings, resume building, and application tracking.

- **Job Listings**: Aggregate job listings from various sources.
- **Resume Builder**: Provide templates and tools for creating professional resumes.
- **Application Tracker**: Allow users to track their job applications and statuses.

**Networking**: Offer features for users to connect with mentors, peers, and industry professionals to expand their professional network.

- **Mentorship Programs**: Connect users with potential mentors.
- **Networking Events**: List and recommend industry events and meetups.
- **Professional Groups**: Enable users to join and participate in professional groups and forums.

**Performance Tracking**: Allow users to track their performance and achievements over time, providing insights into their career progress.

- **Achievement Log**: Maintain a log of user achievements and milestones.
- **Performance Reviews**: Facilitate self-assessments and peer reviews.
- **Analytics Dashboard**: Provide a dashboard with insights and analytics on career progress.

## Goal attributes

- **Title**: The name of the goal, which should be clear and precise.
- **Description**: A detailed explanation of the goal, including why it is important and how it can be achieved.
- **Start Date**: The date when the user begins working on the goal.
- **End Date**: The date by which the goal should be achieved.
- **Status**: The current state of the goal (e.g., "In Progress", "Completed", "Not Started").
- **Priority**: The level of importance of the goal (e.g., "High", "Medium", "Low").
- **Progress**: An indicator of the percentage of the goal that has been achieved.
- **Milestones**: Key steps or milestones that need to be reached to progress towards the goal.
- **Resources**: Tools, documents, or contacts necessary to achieve the goal.
- **Comments**: Notes or reflections from the user regarding the goal.
