"""Comprehensive course and internship database for all job role skills."""

from typing import Dict, List, Any

COURSE_DATABASE: Dict[str, Dict[str, Any]] = {
    "Python": {
        "courses": [
            {"course": "Python for Everybody Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python"},
            {"course": "Complete Python Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-python-bootcamp"},
            {"course": "Python 3 Programming Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python-3-programming"},
            {"course": "Python Data Structures", "platform": "edX", "url": "https://www.edx.org/learn/python/python-basics-for-data-science"},
            {"course": "Advanced Python", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/advanced-python"},
        ],
        "internships": [
            {"company": "Google", "role": "Python Developer Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "Microsoft", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://careers.microsoft.com"},
            {"company": "Amazon", "role": "Backend Engineer Intern", "location": "On-site", "url": "https://www.amazon.jobs"},
        ],
    },
    "Java": {
        "courses": [
            {"course": "Java Programming and Software Engineering Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/java-programming"},
            {"course": "Java Programming Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/java-the-complete-java-developer-course"},
            {"course": "Object Oriented Programming in Java", "platform": "edX", "url": "https://www.edx.org/learn/java/object-oriented-programming-in-java"},
            {"course": "Java SE 11 Developer Certification", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/java-se-11-developer-certification-1z0-819"},
            {"course": "Java Enterprise Edition", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/java-enterprise"},
        ],
        "internships": [
            {"company": "Oracle", "role": "Java Developer Intern", "location": "Remote", "url": "https://www.oracle.com/careers"},
            {"company": "IBM", "role": "Software Engineer Intern", "location": "Hybrid", "url": "https://www.ibm.com/careers"},
            {"company": "SAP", "role": "Java Backend Intern", "location": "On-site", "url": "https://jobs.sap.com"},
        ],
    },
    "C++": {
        "courses": [
            {"course": "C++ For C Programmers", "platform": "Coursera", "url": "https://www.coursera.org/learn/c-plus-plus-a"},
            {"course": "Beginning C++ Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/beginning-c-plus-plus-programming"},
            {"course": "Introduction to C++", "platform": "edX", "url": "https://www.edx.org/learn/c/microsoft-introduction-to-c"},
            {"course": "C++ Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cpp-fundamentals"},
            {"course": "Modern C++ Concurrency", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/c-plus-plus"},
        ],
        "internships": [
            {"company": "NVIDIA", "role": "C++ Software Intern", "location": "Remote", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
            {"company": "Bloomberg", "role": "Software Engineering Intern", "location": "On-site", "url": "https://www.bloomberg.com/company/careers"},
            {"company": "Adobe", "role": "C++ Developer Intern", "location": "Hybrid", "url": "https://careers.adobe.com"},
        ],
    },
    "C": {
        "courses": [
            {"course": "C Programming: Getting Started", "platform": "edX", "url": "https://www.edx.org/learn/c/dartmouth-c-programming-getting-started"},
            {"course": "C Programming For Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/c-programming-for-beginners"},
            {"course": "C for Everyone: Programming Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/c-for-everyone"},
            {"course": "Advanced C Programming", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/c"},
            {"course": "Embedded C Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/embedded-c-programming"},
        ],
        "internships": [
            {"company": "Intel", "role": "Firmware Engineering Intern", "location": "On-site", "url": "https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"},
            {"company": "Texas Instruments", "role": "Embedded Software Intern", "location": "Hybrid", "url": "https://careers.ti.com"},
            {"company": "Qualcomm", "role": "Embedded Systems Intern", "location": "On-site", "url": "https://www.qualcomm.com/company/careers"},
        ],
    },
    "R": {
        "courses": [
            {"course": "R Programming", "platform": "Coursera", "url": "https://www.coursera.org/learn/r-programming"},
            {"course": "Data Science with R", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/data-scientist-with-r"},
            {"course": "R for Data Science", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/r-data-science"},
            {"course": "Advanced R Programming", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/r"},
            {"course": "Statistics with R", "platform": "edX", "url": "https://www.edx.org/learn/r/statistics"},
        ],
        "internships": [
            {"company": "RStudio", "role": "Data Science Intern", "location": "Remote", "url": "https://posit.co/careers"},
            {"company": "Biogen", "role": "Biostatistics Intern", "location": "Hybrid", "url": "https://www.biogen.com/careers"},
            {"company": "Pfizer", "role": "R Programming Intern", "location": "On-site", "url": "https://www.pfizer.com/careers"},
        ],
    },
    "JavaScript": {
        "courses": [
            {"course": "JavaScript: The Advanced Concepts", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-javascript-concepts"},
            {"course": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures"},
            {"course": "Modern JavaScript from the Beginning", "platform": "Udemy", "url": "https://www.udemy.com/course/modern-javascript-from-the-beginning"},
            {"course": "JavaScript Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/javascript"},
            {"course": "ES6 JavaScript: The Complete Developer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/javascript-es6"},
        ],
        "internships": [
            {"company": "Netflix", "role": "JavaScript Engineering Intern", "location": "Remote", "url": "https://jobs.netflix.com"},
            {"company": "Uber", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.uber.com/careers"},
            {"company": "Airbnb", "role": "Web Platform Intern", "location": "On-site", "url": "https://careers.airbnb.com"},
        ],
    },
    "Node.js": {
        "courses": [
            {"course": "Node.js, Express, MongoDB Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp"},
            {"course": "Server-side Development with NodeJS", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
            {"course": "Node.js Microservices", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/node-js-microservices"},
            {"course": "Advanced Node.js", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/node-js"},
            {"course": "Node.js Design Patterns", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-design-patterns"},
        ],
        "internships": [
            {"company": "PayPal", "role": "Node.js Developer Intern", "location": "Remote", "url": "https://www.paypal.com/us/webapps/mpp/jobs"},
            {"company": "Slack", "role": "Backend Engineering Intern", "location": "Hybrid", "url": "https://slack.com/careers"},
            {"company": "Medium", "role": "Platform Engineering Intern", "location": "On-site", "url": "https://medium.com/jobs"},
        ],
    },
    "TypeScript": {
        "courses": [
            {"course": "Understanding TypeScript", "platform": "Udemy", "url": "https://www.udemy.com/course/understanding-typescript"},
            {"course": "TypeScript Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/typescript-fundamentals"},
            {"course": "TypeScript: The Complete Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/typescript-the-complete-developers-guide"},
            {"course": "Advanced TypeScript", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/typescript"},
            {"course": "TypeScript with React", "platform": "Coursera", "url": "https://www.coursera.org/learn/typescript"},
        ],
        "internships": [
            {"company": "Linear", "role": "TypeScript Engineering Intern", "location": "Remote", "url": "https://linear.app/careers"},
            {"company": "Notion", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.notion.so/careers"},
            {"company": "Figma", "role": "Web Engineering Intern", "location": "On-site", "url": "https://www.figma.com/careers"},
        ],
    },
    "Data Structures": {
        "courses": [
            {"course": "Data Structures and Algorithms Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/data-structures-algorithms"},
            {"course": "Master the Coding Interview", "platform": "Udemy", "url": "https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms"},
            {"course": "Data Structures Fundamentals", "platform": "edX", "url": "https://www.edx.org/learn/data-structures"},
            {"course": "Algorithms and Data Structures in Python", "platform": "Udemy", "url": "https://www.udemy.com/course/algorithms-and-data-structures-in-python"},
            {"course": "Data Structures in Java", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/data-structures"},
        ],
        "internships": [
            {"company": "Meta", "role": "Software Engineering Intern", "location": "Remote", "url": "https://www.metacareers.com"},
            {"company": "Apple", "role": "Algorithms Engineer Intern", "location": "On-site", "url": "https://jobs.apple.com"},
            {"company": "LinkedIn", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://careers.linkedin.com"},
        ],
    },
    "Algorithms": {
        "courses": [
            {"course": "Algorithmic Toolbox", "platform": "Coursera", "url": "https://www.coursera.org/learn/algorithmic-toolbox"},
            {"course": "Algorithms Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/algorithms"},
            {"course": "Grokking the Coding Interview", "platform": "Educative", "url": "https://www.educative.io/courses/grokking-the-coding-interview"},
            {"course": "Introduction to Algorithms", "platform": "MIT OpenCourseWare", "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011"},
            {"course": "Competitive Programming", "platform": "Codeforces", "url": "https://codeforces.com/edu/course/2"},
        ],
        "internships": [
            {"company": "Two Sigma", "role": "Quantitative Research Intern", "location": "On-site", "url": "https://www.twosigma.com/careers"},
            {"company": "Jane Street", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://www.janestreet.com/join-jane-street"},
            {"company": "Citadel", "role": "Algorithm Engineering Intern", "location": "On-site", "url": "https://www.citadel.com/careers"},
        ],
    },
    "OOP": {
        "courses": [
            {"course": "Object-Oriented Programming in Java", "platform": "Coursera", "url": "https://www.coursera.org/learn/object-oriented-java"},
            {"course": "OOP in Python", "platform": "Udemy", "url": "https://www.udemy.com/course/object-oriented-programming-python"},
            {"course": "Design Patterns in OOP", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/design-patterns-overview"},
            {"course": "SOLID Principles", "platform": "Coursera", "url": "https://www.coursera.org/learn/solid-principles-object-oriented-design"},
            {"course": "OOP Design Patterns", "platform": "edX", "url": "https://www.edx.org/learn/object-oriented-programming"},
        ],
        "internships": [
            {"company": "Salesforce", "role": "Software Engineering Intern", "location": "Remote", "url": "https://careers.salesforce.com"},
            {"company": "Oracle", "role": "Java OOP Developer Intern", "location": "Hybrid", "url": "https://www.oracle.com/careers"},
            {"company": "Intuit", "role": "Software Engineering Intern", "location": "On-site", "url": "https://www.intuit.com/careers"},
        ],
    },
    "Git": {
        "courses": [
            {"course": "Git and GitHub Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/google-it-automation"},
            {"course": "Git Complete: The Definitive Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/git-complete"},
            {"course": "GitHub Actions", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/github"},
            {"course": "Advanced Git", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/advanced-git"},
            {"course": "Git Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-git"},
        ],
        "internships": [
            {"company": "GitHub", "role": "Software Engineering Intern", "location": "Remote", "url": "https://github.com/about/careers"},
            {"company": "GitLab", "role": "Engineering Intern", "location": "Remote", "url": "https://about.gitlab.com/jobs"},
            {"company": "Atlassian", "role": "DevOps Intern", "location": "Hybrid", "url": "https://www.atlassian.com/company/careers"},
        ],
    },
    "SQL": {
        "courses": [
            {"course": "SQL for Data Science", "platform": "Coursera", "url": "https://www.coursera.org/learn/sql-for-data-science"},
            {"course": "The Complete SQL Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-sql-bootcamp"},
            {"course": "Introduction to SQL", "platform": "edX", "url": "https://www.edx.org/learn/sql"},
            {"course": "Advanced SQL", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/advanced-sql"},
            {"course": "SQL Querying", "platform": "Khan Academy", "url": "https://www.khanacademy.org/computing/computer-programming/sql"},
        ],
        "internships": [
            {"company": "Snowflake", "role": "Data Engineering Intern", "location": "Remote", "url": "https://careers.snowflake.com"},
            {"company": "Databricks", "role": "SQL Analytics Intern", "location": "Hybrid", "url": "https://www.databricks.com/company/careers"},
            {"company": "MongoDB", "role": "Database Engineering Intern", "location": "On-site", "url": "https://www.mongodb.com/careers"},
        ],
    },
    "Linux": {
        "courses": [
            {"course": "Linux Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/linux-fundamentals"},
            {"course": "Linux Administration Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/linux-administration-bootcamp"},
            {"course": "Introduction to Linux", "platform": "edX", "url": "https://www.edx.org/learn/linux"},
            {"course": "Linux Command Line Basics", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-the-command-line"},
            {"course": "Red Hat Certified System Administrator", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/red-hat-system-administrator"},
        ],
        "internships": [
            {"company": "Red Hat", "role": "Linux Engineering Intern", "location": "Remote", "url": "https://www.redhat.com/en/jobs"},
            {"company": "Canonical", "role": "Ubuntu Engineering Intern", "location": "Remote", "url": "https://canonical.com/careers"},
            {"company": "SUSE", "role": "Systems Engineering Intern", "location": "Hybrid", "url": "https://www.suse.com/careers"},
        ],
    },
    "REST APIs": {
        "courses": [
            {"course": "APIs and Microservices", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/apis-and-microservices"},
            {"course": "REST API Design", "platform": "Udemy", "url": "https://www.udemy.com/course/rest-api-design"},
            {"course": "Building RESTful APIs with Node.js", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
            {"course": "API Testing with Postman", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/api"},
            {"course": "GraphQL and REST API Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/designing-restful-web-apis"},
        ],
        "internships": [
            {"company": "Stripe", "role": "API Engineering Intern", "location": "Remote", "url": "https://stripe.com/jobs"},
            {"company": "Twilio", "role": "Developer Relations Intern", "location": "Hybrid", "url": "https://www.twilio.com/company/jobs"},
            {"company": "SendGrid", "role": "API Developer Intern", "location": "On-site", "url": "https://sendgrid.com/careers"},
        ],
    },
    "RESTful APIs": {
        "courses": [
            {"course": "REST API Design, Development", "platform": "Udemy", "url": "https://www.udemy.com/course/rest-api-design"},
            {"course": "APIs and Microservices", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/apis-and-microservices"},
            {"course": "Web Services and APIs", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
            {"course": "Building REST APIs with Django", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/api"},
            {"course": "REST API with Spring Boot", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/rest-api-spring-boot"},
        ],
        "internships": [
            {"company": "Stripe", "role": "API Engineering Intern", "location": "Remote", "url": "https://stripe.com/jobs"},
            {"company": "Postman", "role": "API Platform Intern", "location": "Hybrid", "url": "https://www.postman.com/careers"},
            {"company": "RapidAPI", "role": "Developer Experience Intern", "location": "On-site", "url": "https://rapidapi.com/careers"},
        ],
    },
    "Testing": {
        "courses": [
            {"course": "Software Testing and Automation", "platform": "Coursera", "url": "https://www.coursera.org/specializations/software-testing-automation"},
            {"course": "Automation Testing with Selenium", "platform": "Udemy", "url": "https://www.udemy.com/course/selenium-webdriver-with-java"},
            {"course": "Test-Driven Development", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/test-driven-development-big-picture"},
            {"course": "Software Testing Fundamentals", "platform": "edX", "url": "https://www.edx.org/learn/software-testing"},
            {"course": "Playwright Test Automation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/playwright"},
        ],
        "internships": [
            {"company": "BrowserStack", "role": "QA Engineering Intern", "location": "Remote", "url": "https://www.browserstack.com/careers"},
            {"company": "Sauce Labs", "role": "Test Automation Intern", "location": "Hybrid", "url": "https://saucelabs.com/company/careers"},
            {"company": "Applitools", "role": "Visual AI Testing Intern", "location": "On-site", "url": "https://applitools.com/careers"},
        ],
    },
    "CI/CD": {
        "courses": [
            {"course": "DevOps, CI/CD", "platform": "Coursera", "url": "https://www.coursera.org/learn/introduction-to-devops"},
            {"course": "Jenkins, From Zero to Hero", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero"},
            {"course": "GitHub Actions for CI/CD", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/github-actions"},
            {"course": "Azure DevOps Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/azure-devops-getting-started"},
            {"course": "CI/CD with GitLab", "platform": "Udemy", "url": "https://www.udemy.com/course/gitlab-ci-pipelines"},
        ],
        "internships": [
            {"company": "CircleCI", "role": "Developer Experience Intern", "location": "Remote", "url": "https://circleci.com/careers"},
            {"company": "GitLab", "role": "CI/CD Engineering Intern", "location": "Remote", "url": "https://about.gitlab.com/jobs"},
            {"company": "Travis CI", "role": "DevOps Engineering Intern", "location": "Hybrid", "url": "https://www.travis-ci.com/careers"},
        ],
    },
    "Deployment": {
        "courses": [
            {"course": "Deploying Applications with Kubernetes", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/deploying-applications-kubernetes"},
            {"course": "AWS Deployment Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-deployment"},
            {"course": "Heroku Deployment Mastery", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/heroku"},
            {"course": "Docker Deployment", "platform": "Coursera", "url": "https://www.coursera.org/learn/deploying-apps-with-docker"},
            {"course": "Vercel and Netlify Deployment", "platform": "Udemy", "url": "https://www.udemy.com/course/deployment-vercel-netlify"},
        ],
        "internships": [
            {"company": "Vercel", "role": "Platform Engineering Intern", "location": "Remote", "url": "https://vercel.com/careers"},
            {"company": "Heroku", "role": "Infrastructure Intern", "location": "Hybrid", "url": "https://www.heroku.com/careers"},
            {"company": "DigitalOcean", "role": "Cloud Engineering Intern", "location": "On-site", "url": "https://www.digitalocean.com/careers"},
        ],
    },
    "Caching": {
        "courses": [
            {"course": "Redis Caching Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/redis-caching"},
            {"course": "System Design: Caching Strategies", "platform": "Educative", "url": "https://www.educative.io/courses/grokking-system-design"},
            {"course": "Memcached and Redis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/redis-fundamentals"},
            {"course": "CDN and Edge Caching", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/caching"},
            {"course": "High Performance Caching", "platform": "Coursera", "url": "https://www.coursera.org/learn/scalable-software-architecture"},
        ],
        "internships": [
            {"company": "Redis", "role": "Software Engineering Intern", "location": "Remote", "url": "https://redis.com/careers"},
            {"company": "Cloudflare", "role": "Edge Computing Intern", "location": "Hybrid", "url": "https://www.cloudflare.com/careers"},
            {"company": "Fastly", "role": "Caching Infrastructure Intern", "location": "On-site", "url": "https://www.fastly.com/careers"},
        ],
    },
    "Authentication": {
        "courses": [
            {"course": "OAuth 2.0 and OpenID Connect", "platform": "Udemy", "url": "https://www.udemy.com/course/oauth-2-and-openid-connect"},
            {"course": "Authentication and Authorization", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/authentication-authorization-asp-dot-net-core"},
            {"course": "JSON Web Tokens (JWT)", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/authentication"},
            {"course": "Identity and Access Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/identity-and-access-management"},
            {"course": "SSO and SAML", "platform": "Udemy", "url": "https://www.udemy.com/course/saml-sso"},
        ],
        "internships": [
            {"company": "Okta", "role": "Identity Engineering Intern", "location": "Remote", "url": "https://www.okta.com/company/careers"},
            {"company": "Auth0", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://auth0.com/careers"},
            {"company": "Ping Identity", "role": "IAM Engineering Intern", "location": "On-site", "url": "https://www.pingidentity.com/en/company/careers"},
        ],
    },
    "Databases": {
        "courses": [
            {"course": "Database Systems Concepts", "platform": "Coursera", "url": "https://www.coursera.org/learn/database-systems"},
            {"course": "MongoDB Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/mongodb-the-complete-developers-guide"},
            {"course": "PostgreSQL Advanced", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/postgresql-fundamentals"},
            {"course": "Database Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/database-management"},
            {"course": "NoSQL Database Essentials", "platform": "edX", "url": "https://www.edx.org/learn/nosql-databases"},
        ],
        "internships": [
            {"company": "MongoDB", "role": "Database Engineering Intern", "location": "Remote", "url": "https://www.mongodb.com/careers"},
            {"company": "Cockroach Labs", "role": "Distributed Systems Intern", "location": "Hybrid", "url": "https://www.cockroachlabs.com/careers"},
            {"company": "Neo4j", "role": "Graph Database Intern", "location": "On-site", "url": "https://neo4j.com/careers"},
        ],
    },
    "Microservices": {
        "courses": [
            {"course": "Microservices with Spring Boot", "platform": "Udemy", "url": "https://www.udemy.com/course/microservices-with-spring-boot-and-spring-cloud"},
            {"course": "Building Microservices", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/building-microservices"},
            {"course": "Microservices Architecture", "platform": "Coursera", "url": "https://www.coursera.org/learn/microservices"},
            {"course": "AWS Microservices", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/microservices"},
            {"course": "Microservices Patterns", "platform": "edX", "url": "https://www.edx.org/learn/microservices"},
        ],
        "internships": [
            {"company": "Netflix", "role": "Microservices Engineering Intern", "location": "Remote", "url": "https://jobs.netflix.com"},
            {"company": "Uber", "role": "Platform Engineering Intern", "location": "Hybrid", "url": "https://www.uber.com/careers"},
            {"company": "Lyft", "role": "Distributed Systems Intern", "location": "On-site", "url": "https://www.lyft.com/careers"},
        ],
    },
    "HTML": {
        "courses": [
            {"course": "HTML and CSS Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-html"},
            {"course": "HTML5 from Scratch", "platform": "Udemy", "url": "https://www.udemy.com/course/html5-from-scratch"},
            {"course": "Web Design for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/web-design"},
            {"course": "HTML Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/html"},
            {"course": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design"},
        ],
        "internships": [
            {"company": "Vercel", "role": "Frontend Engineering Intern", "location": "Remote", "url": "https://vercel.com/careers"},
            {"company": "Shopify", "role": "Web Developer Intern", "location": "Hybrid", "url": "https://www.shopify.com/careers"},
            {"company": "Wix", "role": "Web Platform Intern", "location": "On-site", "url": "https://www.wix.com/jobs"},
        ],
    },
    "CSS": {
        "courses": [
            {"course": "Advanced CSS and Sass", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-css-and-sass"},
            {"course": "CSS Grid and Flexbox", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/css"},
            {"course": "Modern CSS", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/modern-css"},
            {"course": "CSS Animation Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/css-animation"},
            {"course": "Tailwind CSS Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-tailwind-css"},
        ],
        "internships": [
            {"company": "Figma", "role": "Design Engineering Intern", "location": "Remote", "url": "https://www.figma.com/careers"},
            {"company": "Canva", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.canva.com/careers"},
            {"company": "Webflow", "role": "Web Design Intern", "location": "On-site", "url": "https://webflow.com/careers"},
        ],
    },
    "React": {
        "courses": [
            {"course": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux"},
            {"course": "Front-End Web Development with React", "platform": "Coursera", "url": "https://www.coursera.org/learn/front-end-react"},
            {"course": "React.js Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/react-js"},
            {"course": "Advanced React Patterns", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/reactjs-advanced"},
            {"course": "React Native: Advanced Concepts", "platform": "Udemy", "url": "https://www.udemy.com/course/react-native-advanced"},
        ],
        "internships": [
            {"company": "Meta", "role": "React Engineering Intern", "location": "Remote", "url": "https://www.metacareers.com"},
            {"company": "Vercel", "role": "Next.js Engineering Intern", "location": "Hybrid", "url": "https://vercel.com/careers"},
            {"company": "Discord", "role": "Frontend Engineering Intern", "location": "On-site", "url": "https://discord.com/careers"},
        ],
    },
    "Next.js": {
        "courses": [
            {"course": "Next.js 14 Complete Developer Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/nextjs-react-the-complete-guide"},
            {"course": "Full-Stack Development with Next.js", "platform": "Coursera", "url": "https://www.coursera.org/learn/nextjs"},
            {"course": "Next.js Production Patterns", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/nextjs-fundamentals"},
            {"course": "Advanced Next.js", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/next-js"},
            {"course": "Server Components with Next.js", "platform": "Udemy", "url": "https://www.udemy.com/course/nextjs-server-components"},
        ],
        "internships": [
            {"company": "Vercel", "role": "Framework Engineering Intern", "location": "Remote", "url": "https://vercel.com/careers"},
            {"company": "Notion", "role": "Full Stack Engineering Intern", "location": "Hybrid", "url": "https://www.notion.so/careers"},
            {"company": "HashiCorp", "role": "Developer Tools Intern", "location": "On-site", "url": "https://www.hashicorp.com/careers"},
        ],
    },
    "Responsive Design": {
        "courses": [
            {"course": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design"},
            {"course": "Mobile-First Responsive Design", "platform": "Udemy", "url": "https://www.udemy.com/course/mobile-first-responsive-design"},
            {"course": "Responsive Design with CSS", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/responsive-design"},
            {"course": "Bootstrap 5 From Scratch", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/bootstrap-5-fundamentals"},
            {"course": "Material UI Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/material-design"},
        ],
        "internships": [
            {"company": "Apple", "role": "UI Engineering Intern", "location": "Remote", "url": "https://jobs.apple.com"},
            {"company": "Spotify", "role": "Design Engineering Intern", "location": "Hybrid", "url": "https://www.lifeatspotify.com/jobs"},
            {"company": "Pinterest", "role": "Web Platform Intern", "location": "On-site", "url": "https://www.pinterestcareers.com"},
        ],
    },
    "Accessibility": {
        "courses": [
            {"course": "Web Accessibility", "platform": "Coursera", "url": "https://www.coursera.org/learn/web-accessibility"},
            {"course": "Accessibility for Web Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/accessibility"},
            {"course": "A11y Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/web-accessibility-testing"},
            {"course": "WCAG 2.1 Compliance", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/web-accessibility-wcag"},
            {"course": "Inclusive Design", "platform": "edX", "url": "https://www.edx.org/learn/accessibility"},
        ],
        "internships": [
            {"company": "Deque Systems", "role": "A11y Engineering Intern", "location": "Remote", "url": "https://www.deque.com/company/careers"},
            {"company": "Microsoft", "role": "Inclusive Design Intern", "location": "Hybrid", "url": "https://careers.microsoft.com"},
            {"company": "Apple", "role": "Accessibility Engineering Intern", "location": "On-site", "url": "https://jobs.apple.com"},
        ],
    },
    "Performance Optimization": {
        "courses": [
            {"course": "Web Performance Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/web-performance"},
            {"course": "High Performance Browser Networking", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/web-performance"},
            {"course": "Core Web Vitals", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/web-performance"},
            {"course": "Frontend Performance", "platform": "Coursera", "url": "https://www.coursera.org/learn/frontend-performance"},
            {"course": "Lighthouse and PageSpeed", "platform": "Udemy", "url": "https://www.udemy.com/course/lighthouse-pagespeed"},
        ],
        "internships": [
            {"company": "Google", "role": "Chrome Performance Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "Cloudflare", "role": "Edge Performance Intern", "location": "Hybrid", "url": "https://www.cloudflare.com/careers"},
            {"company": "Akamai", "role": "CDN Performance Intern", "location": "On-site", "url": "https://www.akamai.com/company/careers"},
        ],
    },
    "State Management": {
        "courses": [
            {"course": "Redux Toolkit Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/redux-toolkit-complete-guide"},
            {"course": "Zustand and React State", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/react-state-management"},
            {"course": "Context API and Hooks", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/react-state-management"},
            {"course": "MobX State Management", "platform": "Udemy", "url": "https://www.udemy.com/course/mobx-state-management"},
            {"course": "Recoil for React", "platform": "Coursera", "url": "https://www.coursera.org/learn/react-state-management"},
        ],
        "internships": [
            {"company": "Meta", "role": "React State Intern", "location": "Remote", "url": "https://www.metacareers.com"},
            {"company": "Vercel", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://vercel.com/careers"},
            {"company": "Redux", "role": "Open Source Intern", "location": "On-site", "url": "https://redux.js.org"},
        ],
    },
    "SEO": {
        "courses": [
            {"course": "SEO Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/seo"},
            {"course": "Technical SEO", "platform": "Udemy", "url": "https://www.udemy.com/course/technical-seo"},
            {"course": "SEO Fundamentals", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/seo"},
            {"course": "Advanced SEO Strategies", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/seo-fundamentals"},
            {"course": "Content SEO Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/content-seo"},
        ],
        "internships": [
            {"company": "HubSpot", "role": "SEO Engineering Intern", "location": "Remote", "url": "https://www.hubspot.com/careers"},
            {"company": "Semrush", "role": "SEO Tools Intern", "location": "Hybrid", "url": "https://www.semrush.com/company/careers"},
            {"company": "Ahrefs", "role": "Technical SEO Intern", "location": "On-site", "url": "https://ahrefs.com/careers"},
        ],
    },
    "Machine Learning": {
        "courses": [
            {"course": "Machine Learning Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning-introduction"},
            {"course": "Machine Learning A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/machinelearning"},
            {"course": "Applied Machine Learning", "platform": "edX", "url": "https://www.edx.org/learn/machine-learning"},
            {"course": "Hands-On Machine Learning", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/machine-learning-fundamentals"},
            {"course": "Machine Learning with Python", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/machine-learning-with-python"},
        ],
        "internships": [
            {"company": "Google", "role": "Machine Learning Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "Apple", "role": "ML Platform Intern", "location": "Hybrid", "url": "https://jobs.apple.com"},
            {"company": "OpenAI", "role": "Research Intern", "location": "On-site", "url": "https://openai.com/careers"},
        ],
    },
    "Deep Learning": {
        "courses": [
            {"course": "Deep Learning Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/deep-learning"},
            {"course": "Deep Learning A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/deeplearning"},
            {"course": "Neural Networks and Deep Learning", "platform": "Coursera", "url": "https://www.coursera.org/learn/neural-networks-deep-learning"},
            {"course": "Practical Deep Learning", "platform": "fast.ai", "url": "https://www.fast.ai"},
            {"course": "PyTorch Deep Learning", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/pytorch-fundamentals"},
        ],
        "internships": [
            {"company": "DeepMind", "role": "Research Intern", "location": "Remote", "url": "https://deepmind.com/careers"},
            {"company": "NVIDIA", "role": "Deep Learning Intern", "location": "Hybrid", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
            {"company": "Stability AI", "role": "Generative AI Intern", "location": "On-site", "url": "https://stability.ai/careers"},
        ],
    },
    "TensorFlow": {
        "courses": [
            {"course": "TensorFlow Developer Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice"},
            {"course": "TensorFlow 2.0 Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/tensorflow-developer-certificate-machine-learning-zero-to-mastery"},
            {"course": "TensorFlow.js", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/tensorflow-js-getting-started"},
            {"course": "Advanced TensorFlow", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/tensorflow"},
            {"course": "TensorFlow for Deep Learning", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/deep-learning-with-tensorflow"},
        ],
        "internships": [
            {"company": "Google", "role": "TensorFlow Engineering Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "NVIDIA", "role": "ML Frameworks Intern", "location": "Hybrid", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
            {"company": "Hugging Face", "role": "ML Engineering Intern", "location": "On-site", "url": "https://huggingface.co/careers"},
        ],
    },
    "PyTorch": {
        "courses": [
            {"course": "PyTorch for Deep Learning", "platform": "Udemy", "url": "https://www.udemy.com/course/pytorch-for-deep-learning"},
            {"course": "Deep Learning with PyTorch", "platform": "Coursera", "url": "https://www.coursera.org/learn/deep-neural-networks-with-pytorch"},
            {"course": "PyTorch Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/pytorch-fundamentals"},
            {"course": "Practical PyTorch", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/pytorch"},
            {"course": "PyTorch for Computer Vision", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-deep-learning-with-pytorch"},
        ],
        "internships": [
            {"company": "Meta AI", "role": "PyTorch Engineering Intern", "location": "Remote", "url": "https://www.metacareers.com"},
            {"company": "NVIDIA", "role": "Deep Learning Frameworks Intern", "location": "Hybrid", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
            {"company": "OpenAI", "role": "Research Engineering Intern", "location": "On-site", "url": "https://openai.com/careers"},
        ],
    },
    "Pandas": {
        "courses": [
            {"course": "Data Analysis with Pandas", "platform": "Udemy", "url": "https://www.udemy.com/course/data-analysis-with-pandas"},
            {"course": "Pandas Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/pandas-fundamentals"},
            {"course": "Data Manipulation with Pandas", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/data-manipulation-with-pandas"},
            {"course": "Pandas for Data Science", "platform": "Coursera", "url": "https://www.coursera.org/learn/data-analysis-with-python"},
            {"course": "Advanced Pandas Techniques", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/pandas"},
        ],
        "internships": [
            {"company": "Kaggle", "role": "Data Science Intern", "location": "Remote", "url": "https://www.kaggle.com/careers"},
            {"company": "DataRobot", "role": "ML Engineering Intern", "location": "Hybrid", "url": "https://www.datarobot.com/careers"},
            {"company": "Palantir", "role": "Data Engineering Intern", "location": "On-site", "url": "https://www.palantir.com/careers"},
        ],
    },
    "NumPy": {
        "courses": [
            {"course": "NumPy for Data Science", "platform": "Udemy", "url": "https://www.udemy.com/course/numpy-for-data-science"},
            {"course": "NumPy Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/numpy-fundamentals"},
            {"course": "Scientific Computing with Python", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python"},
            {"course": "NumPy and SciPy", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-numpy"},
            {"course": "Advanced NumPy", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/numpy"},
        ],
        "internships": [
            {"company": "Anaconda", "role": "Scientific Computing Intern", "location": "Remote", "url": "https://www.anaconda.com/careers"},
            {"company": "Quansight", "role": "Open Source Intern", "location": "Hybrid", "url": "https://quansight.com/careers"},
            {"company": "NumFOCUS", "role": "Data Science Intern", "location": "On-site", "url": "https://numfocus.org"},
        ],
    },
    "Matplotlib": {
        "courses": [
            {"course": "Matplotlib for Data Visualization", "platform": "Udemy", "url": "https://www.udemy.com/course/matplotlib-for-data-visualization"},
            {"course": "Data Visualization with Python", "platform": "Coursera", "url": "https://www.coursera.org/learn/python-for-data-visualization"},
            {"course": "Matplotlib Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/matplotlib-fundamentals"},
            {"course": "Python Data Visualization", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/data-visualization"},
            {"course": "Advanced Matplotlib", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib"},
        ],
        "internships": [
            {"company": "Tableau", "role": "Data Visualization Intern", "location": "Remote", "url": "https://www.tableau.com/careers"},
            {"company": "Plotly", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://plotly.com/careers"},
            {"company": "Observable", "role": "Visualization Engineering Intern", "location": "On-site", "url": "https://observablehq.com/careers"},
        ],
    },
    "Statistics": {
        "courses": [
            {"course": "Statistics with Python", "platform": "Coursera", "url": "https://www.coursera.org/specializations/statistics-with-python"},
            {"course": "Practical Statistics", "platform": "Udemy", "url": "https://www.udemy.com/course/statistics-for-data-science"},
            {"course": "Introduction to Statistics", "platform": "edX", "url": "https://www.edx.org/learn/statistics"},
            {"course": "Statistics Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/statistics-fundamentals"},
            {"course": "Bayesian Statistics", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-statistics"},
        ],
        "internships": [
            {"company": "Capital One", "role": "Data Science Intern", "location": "Remote", "url": "https://www.capitalone.com/careers"},
            {"company": "JPMorgan Chase", "role": "Quantitative Research Intern", "location": "Hybrid", "url": "https://www.jpmorganchase.com/careers"},
            {"company": "Goldman Sachs", "role": "Quantitative Analyst Intern", "location": "On-site", "url": "https://www.goldmansachs.com/careers"},
        ],
    },
    "Data Visualization": {
        "courses": [
            {"course": "Data Visualization with Tableau", "platform": "Coursera", "url": "https://www.coursera.org/specializations/data-visualization"},
            {"course": "Data Visualization with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/data-visualization-with-python"},
            {"course": "Information Visualization", "platform": "edX", "url": "https://www.edx.org/learn/data-visualization"},
            {"course": "D3.js Data Visualization", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/d3js-data-visualization-fundamentals"},
            {"course": "Power BI Data Visualization", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/power-bi"},
        ],
        "internships": [
            {"company": "Tableau", "role": "Data Visualization Intern", "location": "Remote", "url": "https://www.tableau.com/careers"},
            {"company": "Looker", "role": "Analytics Engineering Intern", "location": "Hybrid", "url": "https://www.looker.com/careers"},
            {"company": "Mode Analytics", "role": "Data Science Intern", "location": "On-site", "url": "https://mode.com/careers"},
        ],
    },
    "Data Preprocessing": {
        "courses": [
            {"course": "Data Preprocessing with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/data-preprocessing"},
            {"course": "Feature Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/feature-engineering"},
            {"course": "Data Cleaning Fundamentals", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cleaning-data-in-python"},
            {"course": "ETL and Data Pipelines", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/etl-data-warehousing"},
            {"course": "Data Wrangling", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/data-wrangling"},
        ],
        "internships": [
            {"company": "Databricks", "role": "Data Engineering Intern", "location": "Remote", "url": "https://www.databricks.com/company/careers"},
            {"company": "Fivetran", "role": "Data Integration Intern", "location": "Hybrid", "url": "https://www.fivetran.com/careers"},
            {"company": "Stitch Data", "role": "ETL Engineering Intern", "location": "On-site", "url": "https://www.stitchdata.com/careers"},
        ],
    },
    "Model Deployment": {
        "courses": [
            {"course": "ML Model Deployment", "platform": "Udemy", "url": "https://www.udemy.com/course/machine-learning-model-deployment"},
            {"course": "MLOps Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"},
            {"course": "Deploying ML Models", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/deploying-machine-learning-models"},
            {"course": "Kubernetes for ML", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/mlops"},
            {"course": "AWS SageMaker Deployment", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-aws-sagemaker"},
        ],
        "internships": [
            {"company": "Seldon", "role": "ML Engineering Intern", "location": "Remote", "url": "https://www.seldon.io/careers"},
            {"company": "Algorithmia", "role": "ML Platform Intern", "location": "Hybrid", "url": "https://algorithmia.com/careers"},
            {"company": "Weights & Biases", "role": "MLOps Engineering Intern", "location": "On-site", "url": "https://wandb.ai/careers"},
        ],
    },
    "NLP": {
        "courses": [
            {"course": "NLP Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/natural-language-processing"},
            {"course": "NLP with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/nlp-natural-language-processing-with-python"},
            {"course": "Transformers for NLP", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/transformers-natural-language-processing"},
            {"course": "spaCy for NLP", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/natural-language-processing"},
            {"course": "Hugging Face NLP", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-nlp"},
        ],
        "internships": [
            {"company": "Hugging Face", "role": "NLP Engineering Intern", "location": "Remote", "url": "https://huggingface.co/careers"},
            {"company": "AI2", "role": "Research Intern", "location": "Hybrid", "url": "https://allenai.org/careers"},
            {"company": "Grammarly", "role": "NLP Engineering Intern", "location": "On-site", "url": "https://www.grammarly.com/jobs"},
        ],
    },
    "Computer Vision": {
        "courses": [
            {"course": "Computer Vision Basics", "platform": "Coursera", "url": "https://www.coursera.org/learn/computer-vision-basics"},
            {"course": "Deep Learning for Computer Vision", "platform": "Udemy", "url": "https://www.udemy.com/course/deep-learning-computer-vision"},
            {"course": "OpenCV for Computer Vision", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/opencv-fundamentals"},
            {"course": "Advanced Computer Vision", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/computer-vision"},
            {"course": "YOLO and Object Detection", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/object-detection"},
        ],
        "internships": [
            {"company": "Tesla", "role": "Computer Vision Intern", "location": "Remote", "url": "https://www.tesla.com/careers"},
            {"company": "Waymo", "role": "Perception Engineering Intern", "location": "Hybrid", "url": "https://waymo.com/careers"},
            {"company": "Argo AI", "role": "CV Engineering Intern", "location": "On-site", "url": "https://www.argo.ai/careers"},
        ],
    },
    "Docker": {
        "courses": [
            {"course": "Docker and Kubernetes", "platform": "Udemy", "url": "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide"},
            {"course": "Docker Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/docker-fundamentals"},
            {"course": "Containerization with Docker", "platform": "Coursera", "url": "https://www.coursera.org/learn/containerization-docker"},
            {"course": "Docker for Developers", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/docker"},
            {"course": "Advanced Docker", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/docker-for-data-science"},
        ],
        "internships": [
            {"company": "Docker Inc", "role": "Software Engineering Intern", "location": "Remote", "url": "https://www.docker.com/careers"},
            {"company": "Mirantis", "role": "Container Engineering Intern", "location": "Hybrid", "url": "https://www.mirantis.com/careers"},
            {"company": "Portworx", "role": "Storage Engineering Intern", "location": "On-site", "url": "https://portworx.com/careers"},
        ],
    },
    "Kubernetes": {
        "courses": [
            {"course": "Kubernetes for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-kubernetes"},
            {"course": "Certified Kubernetes Administrator", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/certified-kubernetes-administrator"},
            {"course": "Kubernetes Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/google-kubernetes-engine"},
            {"course": "Advanced Kubernetes", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/kubernetes"},
            {"course": "Kubernetes in Production", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/kubernetes-fundamentals"},
        ],
        "internships": [
            {"company": "Google", "role": "Kubernetes Engineering Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "Rancher Labs", "role": "Platform Engineering Intern", "location": "Hybrid", "url": "https://www.rancher.com/careers"},
            {"company": "Red Hat", "role": "OpenShift Engineering Intern", "location": "On-site", "url": "https://www.redhat.com/en/jobs"},
        ],
    },
    "AWS": {
        "courses": [
            {"course": "AWS Solutions Architect", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-certified-solutions-architect-associate"},
            {"course": "AWS Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/aws-fundamentals"},
            {"course": "AWS Developer Certification", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/aws-certified-developer-associate"},
            {"course": "Serverless on AWS", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/amazon-web-services"},
            {"course": "AWS Machine Learning", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-aws"},
        ],
        "internships": [
            {"company": "Amazon Web Services", "role": "Cloud Engineering Intern", "location": "Remote", "url": "https://www.amazon.jobs"},
            {"company": "Cloudflare", "role": "Edge Platform Intern", "location": "Hybrid", "url": "https://www.cloudflare.com/careers"},
            {"company": "Datadog", "role": "Cloud Monitoring Intern", "location": "On-site", "url": "https://www.datadoghq.com/careers"},
        ],
    },
    "Azure": {
        "courses": [
            {"course": "Azure Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/azure-fundamentals"},
            {"course": "Microsoft Azure Certification", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/microsoft-azure-fundamentals"},
            {"course": "Azure Developer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/azure-developer-certification"},
            {"course": "Azure DevOps", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/microsoft-azure"},
            {"course": "Azure Machine Learning", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-azure-ml"},
        ],
        "internships": [
            {"company": "Microsoft", "role": "Azure Engineering Intern", "location": "Remote", "url": "https://careers.microsoft.com"},
            {"company": "HashiCorp", "role": "Cloud Engineering Intern", "location": "Hybrid", "url": "https://www.hashicorp.com/careers"},
            {"company": "Pulumi", "role": "Infrastructure Engineering Intern", "location": "On-site", "url": "https://www.pulumi.com/careers"},
        ],
    },
    "Google Cloud": {
        "courses": [
            {"course": "Google Cloud Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/gcp-fundamentals"},
            {"course": "GCP Professional Certification", "platform": "Udemy", "url": "https://www.udemy.com/course/google-cloud-professional-cloud-architect"},
            {"course": "Google Cloud Essentials", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/google-cloud-platform-essentials"},
            {"course": "GCP Data Engineering", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/google-cloud-platform"},
            {"course": "Serverless GCP", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/introduction-to-gcp"},
        ],
        "internships": [
            {"company": "Google", "role": "Cloud Engineering Intern", "location": "Remote", "url": "https://careers.google.com"},
            {"company": "Elastic", "role": "Search Engineering Intern", "location": "Hybrid", "url": "https://www.elastic.co/careers"},
            {"company": "MongoDB Atlas", "role": "Cloud Engineering Intern", "location": "On-site", "url": "https://www.mongodb.com/careers"},
        ],
    },
    "Terraform": {
        "courses": [
            {"course": "Terraform for AWS", "platform": "Udemy", "url": "https://www.udemy.com/course/terraform-aws"},
            {"course": "Infrastructure as Code with Terraform", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/terraform-getting-started"},
            {"course": "Terraform Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/terraform-for-aws"},
            {"course": "Advanced Terraform", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/terraform"},
            {"course": "Terraform and Vault", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/terraform-fundamentals"},
        ],
        "internships": [
            {"company": "HashiCorp", "role": "Terraform Engineering Intern", "location": "Remote", "url": "https://www.hashicorp.com/careers"},
            {"company": "Spacelift", "role": "Infrastructure Intern", "location": "Hybrid", "url": "https://spacelift.io/careers"},
            {"company": "Env0", "role": "DevOps Engineering Intern", "location": "On-site", "url": "https://www.env0.com/careers"},
        ],
    },
    "Jenkins": {
        "courses": [
            {"course": "Jenkins for DevOps", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero"},
            {"course": "Jenkins Pipeline Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/jenkins-fundamentals"},
            {"course": "Jenkins Administration", "platform": "Coursera", "url": "https://www.coursera.org/learn/jenkins-administration"},
            {"course": "Advanced Jenkins", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/jenkins"},
            {"course": "Jenkins and Docker", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/jenkins-fundamentals"},
        ],
        "internships": [
            {"company": "CloudBees", "role": "Jenkins Engineering Intern", "location": "Remote", "url": "https://www.cloudbees.com/careers"},
            {"company": "JFrog", "role": "DevOps Engineering Intern", "location": "Hybrid", "url": "https://jfrog.com/careers"},
            {"company": "Sonatype", "role": "Security Engineering Intern", "location": "On-site", "url": "https://www.sonatype.com/careers"},
        ],
    },
    "Ansible": {
        "courses": [
            {"course": "Ansible for DevOps", "platform": "Udemy", "url": "https://www.udemy.com/course/ansible-for-devops"},
            {"course": "Ansible Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ansible-fundamentals"},
            {"course": "Red Hat Ansible", "platform": "Coursera", "url": "https://www.coursera.org/learn/ansible-red-hat"},
            {"course": "Advanced Ansible", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/ansible"},
            {"course": "Ansible Automation", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/ansible-fundamentals"},
        ],
        "internships": [
            {"company": "Red Hat", "role": "Automation Engineering Intern", "location": "Remote", "url": "https://www.redhat.com/en/jobs"},
            {"company": "Ansible", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://www.ansible.com/careers"},
            {"company": "Puppet", "role": "Infrastructure Engineering Intern", "location": "On-site", "url": "https://puppet.com/careers"},
        ],
    },
    "Monitoring": {
        "courses": [
            {"course": "Monitoring and Observability", "platform": "Udemy", "url": "https://www.udemy.com/course/monitoring-and-observability"},
            {"course": "Prometheus and Grafana", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/prometheus-grafana-getting-started"},
            {"course": "Datadog Monitoring", "platform": "Coursera", "url": "https://www.coursera.org/learn/monitoring-cloud"},
            {"course": "New Relic Observability", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/observability"},
            {"course": "ELK Stack Monitoring", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/elasticsearch-fundamentals"},
        ],
        "internships": [
            {"company": "Datadog", "role": "Observability Engineering Intern", "location": "Remote", "url": "https://www.datadoghq.com/careers"},
            {"company": "New Relic", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://newrelic.com/careers"},
            {"company": "Dynatrace", "role": "AI Engineering Intern", "location": "On-site", "url": "https://www.dynatrace.com/careers"},
        ],
    },
    "Infrastructure as Code": {
        "courses": [
            {"course": "Infrastructure as Code", "platform": "Udemy", "url": "https://www.udemy.com/course/infrastructure-as-code"},
            {"course": "IaC with Terraform", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/terraform-getting-started"},
            {"course": "CloudFormation and IaC", "platform": "Coursera", "url": "https://www.coursera.org/learn/aws-cloudformation"},
            {"course": "Pulumi Fundamentals", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/infrastructure-as-code"},
            {"course": "AWS CDK", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/aws-cdk-fundamentals"},
        ],
        "internships": [
            {"company": "HashiCorp", "role": "IaC Engineering Intern", "location": "Remote", "url": "https://www.hashicorp.com/careers"},
            {"company": "Pulumi", "role": "Platform Engineering Intern", "location": "Hybrid", "url": "https://www.pulumi.com/careers"},
            {"company": "AWS", "role": "Cloud Engineering Intern", "location": "On-site", "url": "https://www.amazon.jobs"},
        ],
    },
    "Network Security": {
        "courses": [
            {"course": "Network Security Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/network-security"},
            {"course": "CompTIA Security+", "platform": "Udemy", "url": "https://www.udemy.com/course/comptia-security-certification-sy0-601"},
            {"course": "Network Security Essentials", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/network-security-fundamentals"},
            {"course": "Cisco CCNA Security", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/network-security"},
            {"course": "Advanced Network Security", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/network-security"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Security Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "Palo Alto Networks", "role": "Network Security Intern", "location": "Hybrid", "url": "https://www.paloaltonetworks.com/company/careers"},
            {"company": "Fortinet", "role": "Cybersecurity Intern", "location": "On-site", "url": "https://www.fortinet.com/corporate/careers"},
        ],
    },
    "Firewalls": {
        "courses": [
            {"course": "Firewall Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/firewall-fundamentals"},
            {"course": "Palo Alto Firewall", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/palo-alto-firewall-fundamentals"},
            {"course": "Firewall Configuration", "platform": "Coursera", "url": "https://www.coursera.org/learn/network-security"},
            {"course": "Advanced Firewall", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/firewalls"},
            {"course": "pfSense and OPNsense", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/network-security"},
        ],
        "internships": [
            {"company": "Palo Alto Networks", "role": "Firewall Engineering Intern", "location": "Remote", "url": "https://www.paloaltonetworks.com/company/careers"},
            {"company": "Fortinet", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://www.fortinet.com/corporate/careers"},
            {"company": "Check Point", "role": "Network Security Intern", "location": "On-site", "url": "https://www.checkpoint.com/careers"},
        ],
    },
    "Encryption": {
        "courses": [
            {"course": "Cryptography Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/crypto"},
            {"course": "Applied Cryptography", "platform": "Udemy", "url": "https://www.udemy.com/course/applied-cryptography"},
            {"course": "Encryption and Hashing", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cryptography-fundamentals"},
            {"course": "Public Key Infrastructure", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/cryptography"},
            {"course": "Quantum Cryptography", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cryptography-fundamentals"},
        ],
        "internships": [
            {"company": "Cloudflare", "role": "Cryptography Engineering Intern", "location": "Remote", "url": "https://www.cloudflare.com/careers"},
            {"company": "Keybase", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://keybase.io"},
            {"company": "Let's Encrypt", "role": "Security Engineering Intern", "location": "On-site", "url": "https://letsencrypt.org"},
        ],
    },
    "SIEM": {
        "courses": [
            {"course": "SIEM Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/siem-fundamentals"},
            {"course": "Splunk Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/splunk-fundamentals"},
            {"course": "ELK Stack for SIEM", "platform": "Coursera", "url": "https://www.coursera.org/learn/elastic-stack"},
            {"course": "QRadar SIEM", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/siem"},
            {"course": "Splunk Administration", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/splunk-fundamentals"},
        ],
        "internships": [
            {"company": "Splunk", "role": "SIEM Engineering Intern", "location": "Remote", "url": "https://www.splunk.com/careers"},
            {"company": "Elastic", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://www.elastic.co/careers"},
            {"company": "IBM Security", "role": "Cybersecurity Intern", "location": "On-site", "url": "https://www.ibm.com/careers"},
        ],
    },
    "Vulnerability Assessment": {
        "courses": [
            {"course": "Vulnerability Assessment", "platform": "Udemy", "url": "https://www.udemy.com/course/vulnerability-assessment"},
            {"course": "Ethical Hacking", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ethical-hacking-understanding"},
            {"course": "Penetration Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/penetration-testing"},
            {"course": "OWASP Top 10", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/penetration-testing"},
            {"course": "Burp Suite", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/penetration-testing"},
        ],
        "internships": [
            {"company": "Rapid7", "role": "Security Engineering Intern", "location": "Remote", "url": "https://www.rapid7.com/careers"},
            {"company": "Tenable", "role": "Vulnerability Research Intern", "location": "Hybrid", "url": "https://www.tenable.com/careers"},
            {"company": "Qualys", "role": "Security Engineering Intern", "location": "On-site", "url": "https://www.qualys.com/careers"},
        ],
    },
    "Incident Response": {
        "courses": [
            {"course": "Incident Response", "platform": "Udemy", "url": "https://www.udemy.com/course/incident-response"},
            {"course": "DFIR Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/digital-forensics-incident-response"},
            {"course": "Cybersecurity Incident Response", "platform": "Coursera", "url": "https://www.coursera.org/learn/cybersecurity-incident-response"},
            {"course": "SOC Operations", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/incident-response"},
            {"course": "Threat Hunting", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cybersecurity-fundamentals"},
        ],
        "internships": [
            {"company": "Mandiant", "role": "Incident Response Intern", "location": "Remote", "url": "https://www.mandiant.com/careers"},
            {"company": "CrowdStrike", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://www.crowdstrike.com/careers"},
            {"company": "FireEye", "role": "Threat Intelligence Intern", "location": "On-site", "url": "https://www.fireeye.com/careers"},
        ],
    },
    "Risk Management": {
        "courses": [
            {"course": "Risk Management Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/risk-management-fundamentals"},
            {"course": "Cyber Risk Management", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cyber-risk-management"},
            {"course": "Enterprise Risk", "platform": "Coursera", "url": "https://www.coursera.org/learn/operational-risk-management"},
            {"course": "GRC Fundamentals", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/risk-management"},
            {"course": "ISO 27001", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cybersecurity-fundamentals"},
        ],
        "internships": [
            {"company": "ServiceNow", "role": "GRC Engineering Intern", "location": "Remote", "url": "https://www.servicenow.com/careers"},
            {"company": "RSA Security", "role": "Risk Management Intern", "location": "Hybrid", "url": "https://www.rsa.com/careers"},
            {"company": "MetricStream", "role": "Compliance Engineering Intern", "location": "On-site", "url": "https://www.metricstream.com/careers"},
        ],
    },
    "Penetration Testing": {
        "courses": [
            {"course": "Penetration Testing", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-penetration-testing-from-scratch"},
            {"course": "Ethical Hacking", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ethical-hacking-understanding"},
            {"course": "OSCP Preparation", "platform": "Coursera", "url": "https://www.coursera.org/learn/penetration-testing"},
            {"course": "Advanced Penetration Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/penetration-testing"},
            {"course": "Bug Bounty Hunting", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/penetration-testing"},
        ],
        "internships": [
            {"company": "HackerOne", "role": "Bug Bounty Intern", "location": "Remote", "url": "https://www.hackerone.com/careers"},
            {"company": "Bugcrowd", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://www.bugcrowd.com/careers"},
            {"company": "Synack", "role": "Penetration Testing Intern", "location": "On-site", "url": "https://www.synack.com/careers"},
        ],
    },
    "Security Policies": {
        "courses": [
            {"course": "Security Policy Development", "platform": "Udemy", "url": "https://www.udemy.com/course/security-policy-development"},
            {"course": "GRC and Compliance", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cyber-risk-management"},
            {"course": "NIST Cybersecurity Framework", "platform": "Coursera", "url": "https://www.coursera.org/learn/nist-cybersecurity-framework"},
            {"course": "ISO 27001 Implementation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/compliance"},
            {"course": "Security Governance", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cybersecurity-fundamentals"},
        ],
        "internships": [
            {"company": "Coalfire", "role": "Compliance Engineering Intern", "location": "Remote", "url": "https://www.coalfire.com/careers"},
            {"company": "A-LIGN", "role": "Audit Engineering Intern", "location": "Hybrid", "url": "https://a-lign.com/careers"},
            {"company": "Bishop Fox", "role": "Security Consulting Intern", "location": "On-site", "url": "https://www.bishopfox.com/careers"},
        ],
    },
    "TCP/IP": {
        "courses": [
            {"course": "TCP/IP Protocol Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/tcp-ip-fundamentals"},
            {"course": "Networking Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/computer-communications"},
            {"course": "TCP/IP and Networking", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/tcp-ip-networking-fundamentals"},
            {"course": "Advanced TCP/IP", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/networking-protocols"},
            {"course": "Wireshark and Packet Analysis", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/network-analysis"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Network Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "Juniper Networks", "role": "Networking Intern", "location": "Hybrid", "url": "https://www.juniper.net/careers"},
            {"company": "Arista Networks", "role": "Network Engineering Intern", "location": "On-site", "url": "https://www.arista.com/careers"},
        ],
    },
    "Routing": {
        "courses": [
            {"course": "Routing and Switching", "platform": "Udemy", "url": "https://www.udemy.com/course/routing-and-switching"},
            {"course": "Cisco CCNA Routing", "platform": "Coursera", "url": "https://www.coursera.org/learn/networking-basics"},
            {"course": "Advanced Routing", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/routing-fundamentals"},
            {"course": "BGP and OSPF", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/network-routing"},
            {"course": "Software-Defined Networking", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/networking-fundamentals"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Routing Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "VMware", "role": "NSX Engineering Intern", "location": "Hybrid", "url": "https://careers.vmware.com"},
            {"company": "Nokia", "role": "IP Routing Intern", "location": "On-site", "url": "https://www.nokia.com/careers"},
        ],
    },
    "Switching": {
        "courses": [
            {"course": "LAN Switching Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/lan-switching-fundamentals"},
            {"course": "Cisco Switching", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/switching-fundamentals"},
            {"course": "Network Switching", "platform": "Coursera", "url": "https://www.coursera.org/learn/networking-basics"},
            {"course": "VLAN and Trunking", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/network-switching"},
            {"course": "Data Center Switching", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/networking-fundamentals"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Switching Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "Dell Technologies", "role": "Network Engineering Intern", "location": "Hybrid", "url": "https://jobs.dell.com"},
            {"company": "HPE", "role": "Aruba Networking Intern", "location": "On-site", "url": "https://careers.hpe.com"},
        ],
    },
    "VPN": {
        "courses": [
            {"course": "VPN Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/vpn-fundamentals"},
            {"course": "IPSec and SSL VPN", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/vpn-fundamentals"},
            {"course": "WireGuard and OpenVPN", "platform": "Coursera", "url": "https://www.coursera.org/learn/network-security"},
            {"course": "Zero Trust Networking", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/vpn"},
            {"course": "Cloud VPN Solutions", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/network-security"},
        ],
        "internships": [
            {"company": "Cloudflare", "role": "Network Engineering Intern", "location": "Remote", "url": "https://www.cloudflare.com/careers"},
            {"company": "Tailscale", "role": "VPN Engineering Intern", "location": "Hybrid", "url": "https://tailscale.com/careers"},
            {"company": "Perimeter 81", "role": "Security Engineering Intern", "location": "On-site", "url": "https://www.perimeter81.com/careers"},
        ],
    },
    "Network Monitoring": {
        "courses": [
            {"course": "Network Monitoring with Nagios", "platform": "Udemy", "url": "https://www.udemy.com/course/network-monitoring"},
            {"course": "Zabbix Monitoring", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/zabbix-monitoring"},
            {"course": "PRTG and SNMP", "platform": "Coursera", "url": "https://www.coursera.org/learn/network-management"},
            {"course": "Network Performance Monitoring", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/network-monitoring"},
            {"course": "Datadog Network Monitoring", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/network-monitoring"},
        ],
        "internships": [
            {"company": "Datadog", "role": "Network Monitoring Intern", "location": "Remote", "url": "https://www.datadoghq.com/careers"},
            {"company": "SolarWinds", "role": "Network Management Intern", "location": "Hybrid", "url": "https://www.solarwinds.com/careers"},
            {"company": "ManageEngine", "role": "IT Operations Intern", "location": "On-site", "url": "https://www.manageengine.com/careers"},
        ],
    },
    "Troubleshooting": {
        "courses": [
            {"course": "Network Troubleshooting", "platform": "Udemy", "url": "https://www.udemy.com/course/network-troubleshooting"},
            {"course": "IT Troubleshooting Skills", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/it-troubleshooting"},
            {"course": "Systematic Troubleshooting", "platform": "Coursera", "url": "https://www.coursera.org/learn/troubleshooting"},
            {"course": "Advanced Troubleshooting", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/troubleshooting"},
            {"course": "Root Cause Analysis", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/troubleshooting-fundamentals"},
        ],
        "internships": [
            {"company": "ServiceNow", "role": "IT Operations Intern", "location": "Remote", "url": "https://www.servicenow.com/careers"},
            {"company": "PagerDuty", "role": "Incident Management Intern", "location": "Hybrid", "url": "https://www.pagerduty.com/careers"},
            {"company": "Opsgenie", "role": "Operations Engineering Intern", "location": "On-site", "url": "https://www.atlassian.com/software/opsgenie"},
        ],
    },
    "Wireless Networks": {
        "courses": [
            {"course": "Wireless Networking Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/wireless-networking-fundamentals"},
            {"course": "Wi-Fi 6 and 6E", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/wireless-networking-fundamentals"},
            {"course": "CWNA Certification", "platform": "Coursera", "url": "https://www.coursera.org/learn/wireless-communications"},
            {"course": "5G Networks", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/wireless-networking"},
            {"course": "IoT Wireless Protocols", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/wireless-networking"},
        ],
        "internships": [
            {"company": "Ubiquiti", "role": "Wireless Engineering Intern", "location": "Remote", "url": "https://www.ui.com/careers"},
            {"company": "Cambium Networks", "role": "Wireless Engineering Intern", "location": "Hybrid", "url": "https://www.cambiumnetworks.com/careers"},
            {"company": "Ericsson", "role": "5G Engineering Intern", "location": "On-site", "url": "https://www.ericsson.com/careers"},
        ],
    },
    "Subnetting": {
        "courses": [
            {"course": "IP Subnetting Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/ip-subnetting"},
            {"course": "Subnetting Mastery", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ip-subnetting"},
            {"course": "IPv4 and IPv6", "platform": "Coursera", "url": "https://www.coursera.org/learn/networking-basics"},
            {"course": "Advanced Subnetting", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/networking"},
            {"course": "Network Addressing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/networking-fundamentals"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Network Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "ARIN", "role": "Network Operations Intern", "location": "Hybrid", "url": "https://www.arin.net/careers"},
            {"company": "RIPE NCC", "role": "Internet Registry Intern", "location": "On-site", "url": "https://www.ripe.net/careers"},
        ],
    },
    "OSI Model": {
        "courses": [
            {"course": "OSI Model Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/osi-model"},
            {"course": "Network Protocols", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/network-protocols-fundamentals"},
            {"course": "Computer Networking", "platform": "Coursera", "url": "https://www.coursera.org/specializations/computer-communications"},
            {"course": "Protocol Analysis", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/networking-protocols"},
            {"course": "Network Architecture", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/networking-fundamentals"},
        ],
        "internships": [
            {"company": "IETF", "role": "Internet Standards Intern", "location": "Remote", "url": "https://www.ietf.org"},
            {"company": "ICANN", "role": "Internet Governance Intern", "location": "Hybrid", "url": "https://www.icann.org/careers"},
            {"company": "ISOC", "role": "Internet Policy Intern", "location": "On-site", "url": "https://www.internetsociety.org/careers"},
        ],
    },
    "Test Planning": {
        "courses": [
            {"course": "Test Planning and Management", "platform": "Udemy", "url": "https://www.udemy.com/course/test-planning"},
            {"course": "Software Test Planning", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/software-test-planning"},
            {"course": "Test Strategy", "platform": "Coursera", "url": "https://www.coursera.org/learn/software-testing"},
            {"course": "Agile Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/software-testing"},
            {"course": "Risk-Based Testing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/software-testing"},
        ],
        "internships": [
            {"company": "TestRail", "role": "QA Engineering Intern", "location": "Remote", "url": "https://www.gurock.com/careers"},
            {"company": "Xray", "role": "Test Management Intern", "location": "Hybrid", "url": "https://www.getxray.app/careers"},
            {"company": "Zephyr", "role": "Quality Engineering Intern", "location": "On-site", "url": "https://www.smartbear.com/careers"},
        ],
    },
    "Automation": {
        "courses": [
            {"course": "Test Automation Engineering", "platform": "Udemy", "url": "https://www.udemy.com/course/test-automation-engineering"},
            {"course": "Selenium WebDriver", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/selenium-webdriver-getting-started"},
            {"course": "Cypress Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/automated-testing"},
            {"course": "Robot Framework", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/test-automation"},
            {"course": "Appium Mobile Testing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/test-automation"},
        ],
        "internships": [
            {"company": "Selenium", "role": "Open Source Intern", "location": "Remote", "url": "https://www.selenium.dev"},
            {"company": "Cypress.io", "role": "Engineering Intern", "location": "Hybrid", "url": "https://www.cypress.io/careers"},
            {"company": "SmartBear", "role": "Automation Engineering Intern", "location": "On-site", "url": "https://www.smartbear.com/careers"},
        ],
    },
    "Selenium": {
        "courses": [
            {"course": "Selenium with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/selenium-webdriver-with-python"},
            {"course": "Selenium WebDriver Advanced", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/selenium-webdriver-advanced"},
            {"course": "Selenium Grid", "platform": "Coursera", "url": "https://www.coursera.org/learn/automated-testing"},
            {"course": "Selenium 4 Features", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/selenium"},
            {"course": "Selenium Framework Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/selenium-fundamentals"},
        ],
        "internships": [
            {"company": "Sauce Labs", "role": "Selenium Engineering Intern", "location": "Remote", "url": "https://saucelabs.com/company/careers"},
            {"company": "LambdaTest", "role": "Cloud Testing Intern", "location": "Hybrid", "url": "https://www.lambdatest.com/careers"},
            {"company": "BrowserStack", "role": "QA Engineering Intern", "location": "On-site", "url": "https://www.browserstack.com/careers"},
        ],
    },
    "JUnit": {
        "courses": [
            {"course": "JUnit 5 Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/junit-5-fundamentals"},
            {"course": "Java Testing with JUnit", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/junit-5-fundamentals"},
            {"course": "Test-Driven Development with JUnit", "platform": "Coursera", "url": "https://www.coursera.org/learn/software-testing"},
            {"course": "Mockito and JUnit", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/junit"},
            {"course": "Advanced JUnit", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/java-testing"},
        ],
        "internships": [
            {"company": "JetBrains", "role": "Developer Tools Intern", "location": "Remote", "url": "https://www.jetbrains.com/careers"},
            {"company": "IntelliJ", "role": "Java Engineering Intern", "location": "Hybrid", "url": "https://www.jetbrains.com/idea"},
            {"company": "Gradle", "role": "Build Engineering Intern", "location": "On-site", "url": "https://gradle.org/careers"},
        ],
    },
    "Performance Testing": {
        "courses": [
            {"course": "Performance Testing with JMeter", "platform": "Udemy", "url": "https://www.udemy.com/course/performance-testing-jmeter"},
            {"course": "LoadRunner Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/load-testing-fundamentals"},
            {"course": "Gatling Performance Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/performance-testing"},
            {"course": "K6 Load Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/performance-testing"},
            {"course": "NeoLoad Advanced", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/performance-testing"},
        ],
        "internships": [
            {"company": "BlazeMeter", "role": "Performance Engineering Intern", "location": "Remote", "url": "https://www.blazemeter.com/careers"},
            {"company": "Grafana", "role": "Observability Engineering Intern", "location": "Hybrid", "url": "https://grafana.com/careers"},
            {"company": "LoadRunner", "role": "Performance Testing Intern", "location": "On-site", "url": "https://www.microfocus.com/careers"},
        ],
    },
    "Bug Tracking": {
        "courses": [
            {"course": "Jira for QA", "platform": "Udemy", "url": "https://www.udemy.com/course/jira-for-qa"},
            {"course": "Bug Tracking Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/bug-tracking-fundamentals"},
            {"course": "Issue Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/project-management"},
            {"course": "Defect Management", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/bug-tracking"},
            {"course": "Quality Center", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/bug-tracking"},
        ],
        "internships": [
            {"company": "Atlassian", "role": "Jira Engineering Intern", "location": "Remote", "url": "https://www.atlassian.com/company/careers"},
            {"company": "Monday.com", "role": "Product Engineering Intern", "location": "Hybrid", "url": "https://monday.com/careers"},
            {"company": "Linear", "role": "Issue Tracking Intern", "location": "On-site", "url": "https://linear.app/careers"},
        ],
    },
    "API Testing": {
        "courses": [
            {"course": "API Testing with Postman", "platform": "Udemy", "url": "https://www.udemy.com/course/postman-api-testing"},
            {"course": "REST API Testing", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/api-testing-fundamentals"},
            {"course": "GraphQL Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/api-testing"},
            {"course": "SoapUI and REST", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/api-testing"},
            {"course": "Karate DSL", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/api-testing"},
        ],
        "internships": [
            {"company": "Postman", "role": "API Platform Intern", "location": "Remote", "url": "https://www.postman.com/careers"},
            {"company": "SmartBear", "role": "API Testing Intern", "location": "Hybrid", "url": "https://www.smartbear.com/careers"},
            {"company": "Katalon", "role": "Test Automation Intern", "location": "On-site", "url": "https://www.katalon.com/careers"},
        ],
    },
    "Manual Testing": {
        "courses": [
            {"course": "Manual Testing Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/manual-testing"},
            {"course": "Exploratory Testing", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/exploratory-testing"},
            {"course": "Usability Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/user-experience-design"},
            {"course": "Black Box Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/software-testing"},
            {"course": "User Acceptance Testing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/software-testing"},
        ],
        "internships": [
            {"company": "UserTesting", "role": "UX Research Intern", "location": "Remote", "url": "https://www.usertesting.com/careers"},
            {"company": "Testlio", "role": "QA Engineering Intern", "location": "Hybrid", "url": "https://testlio.com/careers"},
            {"company": "Applause", "role": "Crowdtesting Intern", "location": "On-site", "url": "https://www.applause.com/careers"},
        ],
    },
    "Regression Testing": {
        "courses": [
            {"course": "Regression Testing Strategies", "platform": "Udemy", "url": "https://www.udemy.com/course/regression-testing"},
            {"course": "Test Automation for Regression", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/regression-testing"},
            {"course": "Continuous Testing", "platform": "Coursera", "url": "https://www.coursera.org/learn/continuous-testing"},
            {"course": "Visual Regression Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/regression-testing"},
            {"course": "Automated Regression", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/regression-testing"},
        ],
        "internships": [
            {"company": "Chromatic", "role": "Visual Testing Intern", "location": "Remote", "url": "https://www.chromatic.com/careers"},
            {"company": "Percy", "role": "Visual Regression Intern", "location": "Hybrid", "url": "https://percy.io/careers"},
            {"company": "BackstopJS", "role": "Testing Engineering Intern", "location": "On-site", "url": "https://github.com/garris/BackstopJS"},
        ],
    },
    "Windows Server": {
        "courses": [
            {"course": "Windows Server Administration", "platform": "Udemy", "url": "https://www.udemy.com/course/windows-server-administration"},
            {"course": "Active Directory Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/active-directory-fundamentals"},
            {"course": "Windows Server 2022", "platform": "Coursera", "url": "https://www.coursera.org/learn/windows-server-management"},
            {"course": "PowerShell Scripting", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/windows-server"},
            {"course": "Azure AD Connect", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/windows-server"},
        ],
        "internships": [
            {"company": "Microsoft", "role": "Windows Engineering Intern", "location": "Remote", "url": "https://careers.microsoft.com"},
            {"company": "VMware", "role": "Virtualization Engineering Intern", "location": "Hybrid", "url": "https://careers.vmware.com"},
            {"company": "Citrix", "role": "Systems Engineering Intern", "location": "On-site", "url": "https://www.citrix.com/careers"},
        ],
    },
    "Scripting": {
        "courses": [
            {"course": "Shell Scripting", "platform": "Udemy", "url": "https://www.udemy.com/course/shell-scripting"},
            {"course": "PowerShell for Sysadmins", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/powershell-for-sysadmins"},
            {"course": "Python Scripting", "platform": "Coursera", "url": "https://www.coursera.org/learn/python-scripting"},
            {"course": "Bash Scripting", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/shell-scripting"},
            {"course": "Perl and Ruby Scripting", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/scripting"},
        ],
        "internships": [
            {"company": "Red Hat", "role": "Automation Engineering Intern", "location": "Remote", "url": "https://www.redhat.com/en/jobs"},
            {"company": "Puppet", "role": "Infrastructure Engineering Intern", "location": "Hybrid", "url": "https://puppet.com/careers"},
            {"company": "Chef", "role": "DevOps Engineering Intern", "location": "On-site", "url": "https://www.chef.io/careers"},
        ],
    },
    "Infrastructure": {
        "courses": [
            {"course": "IT Infrastructure", "platform": "Udemy", "url": "https://www.udemy.com/course/it-infrastructure"},
            {"course": "Data Center Infrastructure", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/data-center-infrastructure"},
            {"course": "Cloud Infrastructure", "platform": "Coursera", "url": "https://www.coursera.org/learn/cloud-infrastructure"},
            {"course": "Server Infrastructure", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/infrastructure"},
            {"course": "Hyperconverged Infrastructure", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/infrastructure"},
        ],
        "internships": [
            {"company": "Nutanix", "role": "Infrastructure Engineering Intern", "location": "Remote", "url": "https://www.nutanix.com/careers"},
            {"company": "Pure Storage", "role": "Storage Engineering Intern", "location": "Hybrid", "url": "https://www.purestorage.com/careers"},
            {"company": "NetApp", "role": "Data Management Intern", "location": "On-site", "url": "https://www.netapp.com/careers"},
        ],
    },
    "Virtualization": {
        "courses": [
            {"course": "VMware vSphere", "platform": "Udemy", "url": "https://www.udemy.com/course/vmware-vsphere"},
            {"course": "Hyper-V Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/hyper-v-fundamentals"},
            {"course": "KVM and QEMU", "platform": "Coursera", "url": "https://www.coursera.org/learn/virtualization"},
            {"course": "Proxmox VE", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/virtualization"},
            {"course": "VirtualBox and Vagrant", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/virtualization"},
        ],
        "internships": [
            {"company": "VMware", "role": "Virtualization Engineering Intern", "location": "Remote", "url": "https://careers.vmware.com"},
            {"company": "Citrix", "role": "Virtual Apps Intern", "location": "Hybrid", "url": "https://www.citrix.com/careers"},
            {"company": "Parallels", "role": "Virtualization Engineering Intern", "location": "On-site", "url": "https://www.parallels.com/careers"},
        ],
    },
    "Security": {
        "courses": [
            {"course": "Systems Security", "platform": "Udemy", "url": "https://www.udemy.com/course/systems-security"},
            {"course": "Endpoint Security", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/endpoint-security"},
            {"course": "Identity Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/identity-and-access-management"},
            {"course": "Zero Trust Security", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/systems-security"},
            {"course": "SIEM and SOAR", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/systems-security"},
        ],
        "internships": [
            {"company": "CrowdStrike", "role": "Endpoint Security Intern", "location": "Remote", "url": "https://www.crowdstrike.com/careers"},
            {"company": "SentinelOne", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://www.sentinelone.com/careers"},
            {"company": "Cybereason", "role": "Threat Hunting Intern", "location": "On-site", "url": "https://www.cybereason.com/careers"},
        ],
    },
    "Microcontrollers": {
        "courses": [
            {"course": "Arduino Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/arduino-programming"},
            {"course": "STM32 Microcontrollers", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/stm32-fundamentals"},
            {"course": "Embedded C for Microcontrollers", "platform": "Coursera", "url": "https://www.coursera.org/learn/embedded-systems"},
            {"course": "PIC Microcontrollers", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/microcontrollers"},
            {"course": "Raspberry Pi Programming", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/embedded-systems"},
        ],
        "internships": [
            {"company": "Arduino", "role": "Embedded Engineering Intern", "location": "Remote", "url": "https://www.arduino.cc/careers"},
            {"company": "STMicroelectronics", "role": "MCU Engineering Intern", "location": "Hybrid", "url": "https://www.st.com/careers"},
            {"company": "Microchip", "role": "Embedded Systems Intern", "location": "On-site", "url": "https://www.microchip.com/careers"},
        ],
    },
    "RTOS": {
        "courses": [
            {"course": "FreeRTOS Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/freertos-fundamentals"},
            {"course": "Real-Time Operating Systems", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/rtos-fundamentals"},
            {"course": "RTOS for Embedded Systems", "platform": "Coursera", "url": "https://www.coursera.org/learn/embedded-systems"},
            {"course": "Zephyr RTOS", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/rtos"},
            {"course": "VxWorks Development", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/rtos"},
        ],
        "internships": [
            {"company": "Wind River", "role": "RTOS Engineering Intern", "location": "Remote", "url": "https://www.windriver.com/careers"},
            {"company": "Zephyr Project", "role": "Embedded Engineering Intern", "location": "Hybrid", "url": "https://zephyrproject.org"},
            {"company": "Amazon FreeRTOS", "role": "IoT Engineering Intern", "location": "On-site", "url": "https://www.amazon.jobs"},
        ],
    },
    "Hardware Design": {
        "courses": [
            {"course": "Digital Electronics", "platform": "Udemy", "url": "https://www.udemy.com/course/digital-electronics"},
            {"course": "VHDL and FPGA Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/fpga-fundamentals"},
            {"course": "ASIC Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/vlsi-cad-part1"},
            {"course": "Verilog HDL", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/hardware-design"},
            {"course": "SystemVerilog", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/hardware-design"},
        ],
        "internships": [
            {"company": "AMD", "role": "Hardware Engineering Intern", "location": "Remote", "url": "https://www.amd.com/careers"},
            {"company": "Intel", "role": "SoC Design Intern", "location": "Hybrid", "url": "https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"},
            {"company": "NVIDIA", "role": "ASIC Engineering Intern", "location": "On-site", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
        ],
    },
    "PCB Design": {
        "courses": [
            {"course": "PCB Design with KiCad", "platform": "Udemy", "url": "https://www.udemy.com/course/pcb-design-with-kicad"},
            {"course": "Altium Designer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/altium-designer-fundamentals"},
            {"course": "Eagle PCB Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/electronics"},
            {"course": "PCB Layout", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/pcb-design"},
            {"course": "High-Speed PCB Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/pcb-design"},
        ],
        "internships": [
            {"company": "Altium", "role": "PCB Engineering Intern", "location": "Remote", "url": "https://www.altium.com/careers"},
            {"company": "Cadence", "role": "IC Design Intern", "location": "Hybrid", "url": "https://www.cadence.com/careers"},
            {"company": "Siemens EDA", "role": "PCB Engineering Intern", "location": "On-site", "url": "https://www.sw.siemens.com/careers"},
        ],
    },
    "Signal Processing": {
        "courses": [
            {"course": "Digital Signal Processing", "platform": "Udemy", "url": "https://www.udemy.com/course/digital-signal-processing"},
            {"course": "DSP with MATLAB", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/digital-signal-processing"},
            {"course": "Audio Signal Processing", "platform": "Coursera", "url": "https://www.coursera.org/learn/audio-signal-processing"},
            {"course": "Image Processing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/signal-processing"},
            {"course": "FFT and Spectral Analysis", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/signal-processing"},
        ],
        "internships": [
            {"company": "Shure", "role": "Audio Engineering Intern", "location": "Remote", "url": "https://www.shure.com/careers"},
            {"company": "Bose", "role": "Signal Processing Intern", "location": "Hybrid", "url": "https://www.bose.com/careers"},
            {"company": "Dolby", "role": "Audio R&D Intern", "location": "On-site", "url": "https://www.dolby.com/careers"},
        ],
    },
    "Firmware": {
        "courses": [
            {"course": "Firmware Development", "platform": "Udemy", "url": "https://www.udemy.com/course/firmware-development"},
            {"course": "Embedded Firmware", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/embedded-firmware"},
            {"course": "Bare Metal Programming", "platform": "Coursera", "url": "https://www.coursera.org/learn/embedded-systems"},
            {"course": "UEFI Development", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/firmware"},
            {"course": "Device Drivers", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/firmware"},
        ],
        "internships": [
            {"company": "Apple", "role": "Firmware Engineering Intern", "location": "Remote", "url": "https://jobs.apple.com"},
            {"company": "Western Digital", "role": "Firmware Engineering Intern", "location": "Hybrid", "url": "https://jobs.westerndigital.com"},
            {"company": "Seagate", "role": "Storage Firmware Intern", "location": "On-site", "url": "https://www.seagate.com/careers"},
        ],
    },
    "Debugging": {
        "courses": [
            {"course": "Debugging Techniques", "platform": "Udemy", "url": "https://www.udemy.com/course/debugging-techniques"},
            {"course": "JTAG and SWD Debugging", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/debugging-embedded"},
            {"course": "GDB Debugging", "platform": "Coursera", "url": "https://www.coursera.org/learn/c-programming"},
            {"course": "Oscilloscope Debugging", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/debugging"},
            {"course": "Logic Analyzer", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/debugging"},
        ],
        "internships": [
            {"company": "Segger", "role": "Debug Tool Engineering Intern", "location": "Remote", "url": "https://www.segger.com/careers"},
            {"company": "Lauterbach", "role": "Debugging Intern", "location": "Hybrid", "url": "https://www.lauterbach.com/careers"},
            {"company": "Total Phase", "role": "Hardware Debugging Intern", "location": "On-site", "url": "https://www.totalphase.com/careers"},
        ],
    },
    "Circuit Design": {
        "courses": [
            {"course": "Circuit Analysis", "platform": "Udemy", "url": "https://www.udemy.com/course/circuit-analysis"},
            {"course": "Analog Circuit Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/analog-circuit-design"},
            {"course": "Power Electronics", "platform": "Coursera", "url": "https://www.coursera.org/learn/power-electronics"},
            {"course": "RF Circuit Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/circuit-design"},
            {"course": "PCB Circuit Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/circuit-design"},
        ],
        "internships": [
            {"company": "Texas Instruments", "role": "Analog Engineering Intern", "location": "Remote", "url": "https://careers.ti.com"},
            {"company": "Analog Devices", "role": "Circuit Design Intern", "location": "Hybrid", "url": "https://www.analog.com/careers"},
            {"company": "Maxim Integrated", "role": "Electrical Engineering Intern", "location": "On-site", "url": "https://www.maximintegrated.com/careers"},
        ],
    },
    "Electronics": {
        "courses": [
            {"course": "Electronics Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/electronics-fundamentals"},
            {"course": "Electronic Circuits", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/electronics-fundamentals"},
            {"course": "Semiconductor Devices", "platform": "Coursera", "url": "https://www.coursera.org/learn/semiconductor-devices"},
            {"course": "Power Electronics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/electronics"},
            {"course": "EMC and EMI", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/electronics"},
        ],
        "internships": [
            {"company": "ON Semiconductor", "role": "Device Engineering Intern", "location": "Remote", "url": "https://www.onsemi.com/careers"},
            {"company": "NXP Semiconductors", "role": "Electronics Intern", "location": "Hybrid", "url": "https://www.nxp.com/careers"},
            {"company": "Infineon", "role": "Power Electronics Intern", "location": "On-site", "url": "https://www.infineon.com/careers"},
        ],
    },
    "Power Systems": {
        "courses": [
            {"course": "Power System Analysis", "platform": "Udemy", "url": "https://www.udemy.com/course/power-system-analysis"},
            {"course": "Electrical Power Systems", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/power-systems-fundamentals"},
            {"course": "Smart Grid", "platform": "Coursera", "url": "https://www.coursera.org/learn/smart-grid"},
            {"course": "Renewable Energy Systems", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/power-systems"},
            {"course": "Power Distribution", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/power-systems"},
        ],
        "internships": [
            {"company": "Siemens Energy", "role": "Power Engineering Intern", "location": "Remote", "url": "https://www.siemens-energy.com/careers"},
            {"company": "GE Vernova", "role": "Grid Solutions Intern", "location": "Hybrid", "url": "https://www.ge.com/careers"},
            {"company": "ABB", "role": "Power Systems Intern", "location": "On-site", "url": "https://new.abb.com/careers"},
        ],
    },
    "Matlab": {
        "courses": [
            {"course": "MATLAB Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/matlab-fundamentals"},
            {"course": "MATLAB for Engineers", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/matlab-fundamentals"},
            {"course": "Simulink for Control Systems", "platform": "Coursera", "url": "https://www.coursera.org/learn/matlab"},
            {"course": "MATLAB for Data Analysis", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/matlab"},
            {"course": "Advanced MATLAB", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/matlab"},
        ],
        "internships": [
            {"company": "MathWorks", "role": "MATLAB Engineering Intern", "location": "Remote", "url": "https://www.mathworks.com/company/jobs"},
            {"company": "Boeing", "role": "Engineering Analysis Intern", "location": "Hybrid", "url": "https://jobs.boeing.com"},
            {"company": "Northrop Grumman", "role": "Systems Engineering Intern", "location": "On-site", "url": "https://www.northropgrumman.com/careers"},
        ],
    },
    "Control Systems": {
        "courses": [
            {"course": "Control Systems Engineering", "platform": "Udemy", "url": "https://www.udemy.com/course/control-systems-engineering"},
            {"course": "PID Controller Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/control-systems-fundamentals"},
            {"course": "State Space Control", "platform": "Coursera", "url": "https://www.coursera.org/learn/dynamics-control"},
            {"course": "Robust Control", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/control-systems"},
            {"course": "Model Predictive Control", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/control-systems"},
        ],
        "internships": [
            {"company": "Tesla", "role": "Control Systems Intern", "location": "Remote", "url": "https://www.tesla.com/careers"},
            {"company": "SpaceX", "role": "GNC Engineering Intern", "location": "Hybrid", "url": "https://www.spacex.com/careers"},
            {"company": "Boston Dynamics", "role": "Controls Engineering Intern", "location": "On-site", "url": "https://www.bostondynamics.com/careers"},
        ],
    },
    "Instrumentation": {
        "courses": [
            {"course": "Industrial Instrumentation", "platform": "Udemy", "url": "https://www.udemy.com/course/industrial-instrumentation"},
            {"course": "Process Control Instrumentation", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/instrumentation-fundamentals"},
            {"course": "SCADA Systems", "platform": "Coursera", "url": "https://www.coursera.org/learn/process-control"},
            {"course": "PLC Programming", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/instrumentation"},
            {"course": "HART Protocol", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/instrumentation"},
        ],
        "internships": [
            {"company": "Honeywell", "role": "Instrumentation Engineering Intern", "location": "Remote", "url": "https://careers.honeywell.com"},
            {"company": "Emerson", "role": "Automation Engineering Intern", "location": "Hybrid", "url": "https://www.emerson.com/careers"},
            {"company": "Yokogawa", "role": "Instrumentation Intern", "location": "On-site", "url": "https://www.yokogawa.com/careers"},
        ],
    },
    "Digital Electronics": {
        "courses": [
            {"course": "Digital Logic Design", "platform": "Udemy", "url": "https://www.udemy.com/course/digital-logic-design"},
            {"course": "FPGA Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/fpga-fundamentals"},
            {"course": "VLSI Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/vlsi-cad-part1"},
            {"course": "Digital IC Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/digital-electronics"},
            {"course": "Verilog and VHDL", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/digital-electronics"},
        ],
        "internships": [
            {"company": "Xilinx", "role": "Digital Design Intern", "location": "Remote", "url": "https://www.xilinx.com/careers"},
            {"company": "Lattice Semiconductor", "role": "FPGA Engineering Intern", "location": "Hybrid", "url": "https://www.latticesemi.com/careers"},
            {"company": "Microchip", "role": "Digital IC Intern", "location": "On-site", "url": "https://www.microchip.com/careers"},
        ],
    },
    "Analog Circuits": {
        "courses": [
            {"course": "Analog Circuit Design", "platform": "Udemy", "url": "https://www.udemy.com/course/analog-circuit-design"},
            {"course": "Op-Amp Circuits", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/analog-circuit-design"},
            {"course": "Mixed-Signal Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/analog-circuits"},
            {"course": "RF and Microwave", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/analog-circuits"},
            {"course": "ADC and DAC Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/analog-circuits"},
        ],
        "internships": [
            {"company": "Skyworks", "role": "Analog Engineering Intern", "location": "Remote", "url": "https://www.skyworksinc.com/careers"},
            {"company": "Qorvo", "role": "RF Engineering Intern", "location": "Hybrid", "url": "https://www.qorvo.com/careers"},
            {"company": "Broadcom", "role": "Mixed-Signal Intern", "location": "On-site", "url": "https://www.broadcom.com/careers"},
        ],
    },
    "PCB Layout": {
        "courses": [
            {"course": "PCB Layout Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/pcb-layout-fundamentals"},
            {"course": "High-Speed PCB Layout", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/pcb-layout"},
            {"course": "Multi-Layer PCB Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/electronics"},
            {"course": "EMC PCB Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/pcb-layout"},
            {"course": "Flex PCB Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/pcb-layout"},
        ],
        "internships": [
            {"company": "Sanmina", "role": "PCB Manufacturing Intern", "location": "Remote", "url": "https://www.sanmina.com/careers"},
            {"company": "TTM Technologies", "role": "PCB Engineering Intern", "location": "Hybrid", "url": "https://www.ttm.com/careers"},
            {"company": "Unimicron", "role": "PCB Design Intern", "location": "On-site", "url": "https://www.unimicron.com"},
        ],
    },
    "Semiconductors": {
        "courses": [
            {"course": "Semiconductor Physics", "platform": "Udemy", "url": "https://www.udemy.com/course/semiconductor-physics"},
            {"course": "CMOS Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cmos-design"},
            {"course": "Semiconductor Manufacturing", "platform": "Coursera", "url": "https://www.coursera.org/learn/semiconductor-devices"},
            {"course": "Process Integration", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/semiconductors"},
            {"course": "Yield Engineering", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/semiconductors"},
        ],
        "internships": [
            {"company": "TSMC", "role": "Process Engineering Intern", "location": "Remote", "url": "https://www.tsmc.com/careers"},
            {"company": "Samsung Foundry", "role": "Semiconductor Intern", "location": "Hybrid", "url": "https://www.samsung.com/careers"},
            {"company": "GlobalFoundries", "role": "Manufacturing Intern", "location": "On-site", "url": "https://gf.com/careers"},
        ],
    },
    "CAD": {
        "courses": [
            {"course": "AutoCAD Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/autocad-fundamentals"},
            {"course": "SolidWorks Essentials", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/solidworks-essentials"},
            {"course": "CATIA V5", "platform": "Coursera", "url": "https://www.coursera.org/learn/cad-design"},
            {"course": "Fusion 360", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/cad"},
            {"course": "Inventor Professional", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/cad"},
        ],
        "internships": [
            {"company": "Autodesk", "role": "CAD Engineering Intern", "location": "Remote", "url": "https://www.autodesk.com/careers"},
            {"company": "Dassault Systemes", "role": "PLM Engineering Intern", "location": "Hybrid", "url": "https://www.3ds.com/careers"},
            {"company": "PTC", "role": "Creo Engineering Intern", "location": "On-site", "url": "https://www.ptc.com/careers"},
        ],
    },
    "SolidWorks": {
        "courses": [
            {"course": "SolidWorks Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/solidworks-complete-course"},
            {"course": "SolidWorks Simulation", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/solidworks-simulation"},
            {"course": "SolidWorks Assembly Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/cad-design"},
            {"course": "Sheet Metal Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/solidworks"},
            {"course": "SolidWorks PDM", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/solidworks"},
        ],
        "internships": [
            {"company": "SolidWorks", "role": "Software Engineering Intern", "location": "Remote", "url": "https://www.solidworks.com/careers"},
            {"company": "Fisher Unitech", "role": "Design Engineering Intern", "location": "Hybrid", "url": "https://www.fisherunitech.com/careers"},
            {"company": "GoEngineer", "role": "Technical Support Intern", "location": "On-site", "url": "https://www.goengineer.com/careers"},
        ],
    },
    "Thermodynamics": {
        "courses": [
            {"course": "Thermodynamics Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/thermodynamics-fundamentals"},
            {"course": "Heat Transfer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/heat-transfer"},
            {"course": "CFD for Thermal Analysis", "platform": "Coursera", "url": "https://www.coursera.org/learn/thermodynamics"},
            {"course": "HVAC Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/thermodynamics"},
            {"course": "Combustion Engineering", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/thermodynamics"},
        ],
        "internships": [
            {"company": "Carrier", "role": "HVAC Engineering Intern", "location": "Remote", "url": "https://www.carrier.com/careers"},
            {"company": "Trane", "role": "Thermal Engineering Intern", "location": "Hybrid", "url": "https://www.trane.com/careers"},
            {"company": "Lennox", "role": "Refrigeration Intern", "location": "On-site", "url": "https://www.lennox.com/careers"},
        ],
    },
    "Material Science": {
        "courses": [
            {"course": "Materials Science", "platform": "Udemy", "url": "https://www.udemy.com/course/materials-science"},
            {"course": "Metallurgy Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/metallurgy-fundamentals"},
            {"course": "Composite Materials", "platform": "Coursera", "url": "https://www.coursera.org/learn/materials-science"},
            {"course": "Nanomaterials", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/materials-science"},
            {"course": "Polymer Science", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/materials-science"},
        ],
        "internships": [
            {"company": "BASF", "role": "Materials Science Intern", "location": "Remote", "url": "https://www.basf.com/careers"},
            {"company": "Dow Chemical", "role": "R&D Engineering Intern", "location": "Hybrid", "url": "https://www.dow.com/careers"},
            {"company": "3M", "role": "Materials Engineering Intern", "location": "On-site", "url": "https://www.3m.com/careers"},
        ],
    },
    "Manufacturing": {
        "courses": [
            {"course": "Manufacturing Processes", "platform": "Udemy", "url": "https://www.udemy.com/course/manufacturing-processes"},
            {"course": "CNC Programming", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cnc-programming"},
            {"course": "Lean Manufacturing", "platform": "Coursera", "url": "https://www.coursera.org/learn/lean-manufacturing"},
            {"course": "Additive Manufacturing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/manufacturing"},
            {"course": "Quality in Manufacturing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/manufacturing"},
        ],
        "internships": [
            {"company": "Tesla", "role": "Manufacturing Engineering Intern", "location": "Remote", "url": "https://www.tesla.com/careers"},
            {"company": "Boeing", "role": "Manufacturing Intern", "location": "Hybrid", "url": "https://jobs.boeing.com"},
            {"company": "Protolabs", "role": "Rapid Manufacturing Intern", "location": "On-site", "url": "https://www.protolabs.com/careers"},
        ],
    },
    "Mechanics": {
        "courses": [
            {"course": "Engineering Mechanics", "platform": "Udemy", "url": "https://www.udemy.com/course/engineering-mechanics"},
            {"course": "Statics and Dynamics", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/engineering-mechanics"},
            {"course": "Fluid Mechanics", "platform": "Coursera", "url": "https://www.coursera.org/learn/fluid-mechanics"},
            {"course": "Strength of Materials", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/mechanics"},
            {"course": "Vibrations", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/mechanics"},
        ],
        "internships": [
            {"company": "Lockheed Martin", "role": "Structural Engineering Intern", "location": "Remote", "url": "https://www.lockheedmartin.com/careers"},
            {"company": "Raytheon", "role": "Mechanical Engineering Intern", "location": "Hybrid", "url": "https://www.rtx.com/careers"},
            {"company": "General Dynamics", "role": "Engineering Intern", "location": "On-site", "url": "https://www.gd.com/careers"},
        ],
    },
    "ANSYS": {
        "courses": [
            {"course": "ANSYS Workbench", "platform": "Udemy", "url": "https://www.udemy.com/course/ansys-workbench"},
            {"course": "ANSYS Fluent", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ansys-fluent"},
            {"course": "FEA with ANSYS", "platform": "Coursera", "url": "https://www.coursera.org/learn/finite-element-method"},
            {"course": "ANSYS Mechanical", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/ansys"},
            {"course": "ANSYS CFD", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/ansys"},
        ],
        "internships": [
            {"company": "ANSYS", "role": "Simulation Engineering Intern", "location": "Remote", "url": "https://www.ansys.com/careers"},
            {"company": "Siemens Digital Industries", "role": "Simcenter Intern", "location": "Hybrid", "url": "https://www.sw.siemens.com/careers"},
            {"company": "Altair", "role": "CAE Engineering Intern", "location": "On-site", "url": "https://www.altair.com/careers"},
        ],
    },
    "Product Design": {
        "courses": [
            {"course": "Product Design Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/product-design-fundamentals"},
            {"course": "Design for Manufacturing", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/design-for-manufacturing"},
            {"course": "Industrial Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/product-design"},
            {"course": "Human-Centered Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/product-design"},
            {"course": "Design Thinking", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/product-design"},
        ],
        "internships": [
            {"company": "IDEO", "role": "Design Thinking Intern", "location": "Remote", "url": "https://www.ideo.com/careers"},
            {"company": "Frog Design", "role": "Product Design Intern", "location": "Hybrid", "url": "https://www.frogdesign.com/careers"},
            {"company": "Ammunition", "role": "Industrial Design Intern", "location": "On-site", "url": "https://ammunitiondesign.com/careers"},
        ],
    },
    "Networking": {
        "courses": [
            {"course": "Computer Networking Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/computer-networking-fundamentals"},
            {"course": "Networking Essentials", "platform": "Coursera", "url": "https://www.coursera.org/specializations/computer-communications"},
            {"course": "Network+ Certification", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/comptia-network-plus"},
            {"course": "Cisco Networking Basics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/networking"},
            {"course": "Software-Defined Networking", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/networking-fundamentals"},
        ],
        "internships": [
            {"company": "Cisco", "role": "Network Engineering Intern", "location": "Remote", "url": "https://jobs.cisco.com"},
            {"company": "Juniper Networks", "role": "Networking Intern", "location": "Hybrid", "url": "https://www.juniper.net/careers"},
            {"company": "Arista Networks", "role": "Network Engineering Intern", "location": "On-site", "url": "https://www.arista.com/careers"},
        ],
    },
    "Embedded Systems": {
        "courses": [
            {"course": "Introduction to Embedded Systems", "platform": "Coursera", "url": "https://www.coursera.org/learn/embedded-systems"},
            {"course": "Embedded Systems Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/embedded-systems-programming"},
            {"course": "ARM Cortex-M Programming", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/embedded-systems-arm"},
            {"course": "Real-Time Embedded Systems", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/embedded-systems"},
            {"course": "IoT and Embedded Systems", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/embedded-systems"},
        ],
        "internships": [
            {"company": "ARM", "role": "Embedded Engineering Intern", "location": "Remote", "url": "https://www.arm.com/careers"},
            {"company": "NXP", "role": "Embedded Systems Intern", "location": "Hybrid", "url": "https://www.nxp.com/careers"},
            {"company": "Renesas", "role": "MCU Engineering Intern", "location": "On-site", "url": "https://www.renesas.com/careers"},
        ],
    },
    "Data Analysis": {
        "courses": [
            {"course": "Data Analysis with Python", "platform": "Coursera", "url": "https://www.coursera.org/learn/data-analysis-with-python"},
            {"course": "Data Analyst Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/data-analyst-bootcamp"},
            {"course": "SQL for Data Analysis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/sql-data-analysis"},
            {"course": "Excel for Data Analysis", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/data-analysis"},
            {"course": "Business Analytics", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/data-analysis"},
        ],
        "internships": [
            {"company": "Accenture", "role": "Data Analyst Intern", "location": "Remote", "url": "https://www.accenture.com/careers"},
            {"company": "Deloitte", "role": "Analytics Intern", "location": "Hybrid", "url": "https://www.deloitte.com/careers"},
            {"company": "McKinsey", "role": "Data Analyst Intern", "location": "On-site", "url": "https://www.mckinsey.com/careers"},
        ],
    },
    "Structural Analysis": {
        "courses": [
            {"course": "Structural Analysis Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/structural-analysis"},
            {"course": "Structural Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/structural-engineering"},
            {"course": "Finite Element Analysis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/finite-element-analysis"},
            {"course": "Structural Dynamics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/structural-analysis"},
            {"course": "Seismic Design", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/structural-analysis"},
        ],
        "internships": [
            {"company": "Arup", "role": "Structural Engineering Intern", "location": "Remote", "url": "https://www.arup.com/careers"},
            {"company": "AECOM", "role": "Structural Intern", "location": "Hybrid", "url": "https://aecom.com/careers"},
            {"company": "WSP", "role": "Structural Engineering Intern", "location": "On-site", "url": "https://www.wsp.com/careers"},
        ],
    },
    "Building Design": {
        "courses": [
            {"course": "Building Design and Construction", "platform": "Udemy", "url": "https://www.udemy.com/course/building-design"},
            {"course": "Architectural Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/architectural-design"},
            {"course": "BIM for Building Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/bim-fundamentals"},
            {"course": "Sustainable Building Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/building-design"},
            {"course": "Green Building Certification", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/building-design"},
        ],
        "internships": [
            {"company": "Gensler", "role": "Building Design Intern", "location": "Remote", "url": "https://www.gensler.com/careers"},
            {"company": "HOK", "role": "Architectural Intern", "location": "Hybrid", "url": "https://www.hok.com/careers"},
            {"company": "SOM", "role": "Design Intern", "location": "On-site", "url": "https://www.som.com/careers"},
        ],
    },
    "Material Strength": {
        "courses": [
            {"course": "Strength of Materials", "platform": "Udemy", "url": "https://www.udemy.com/course/strength-of-materials"},
            {"course": "Mechanics of Materials", "platform": "Coursera", "url": "https://www.coursera.org/learn/mechanics-of-materials"},
            {"course": "Material Failure Analysis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/material-failure-analysis"},
            {"course": "Fracture Mechanics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/materials-engineering"},
            {"course": "Fatigue Analysis", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/materials-engineering"},
        ],
        "internships": [
            {"company": "Bechtel", "role": "Materials Engineering Intern", "location": "Remote", "url": "https://www.bechtel.com/careers"},
            {"company": "Fluor", "role": "Engineering Intern", "location": "Hybrid", "url": "https://www.fluor.com/careers"},
            {"company": "Jacobs", "role": "Materials Intern", "location": "On-site", "url": "https://www.jacobs.com/careers"},
        ],
    },
    "Construction Management": {
        "courses": [
            {"course": "Construction Management Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/construction-management"},
            {"course": "Construction Project Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/construction-management"},
            {"course": "BIM for Construction", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/bim-construction"},
            {"course": "Lean Construction", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/construction-management"},
            {"course": "Cost Estimation", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/construction-management"},
        ],
        "internships": [
            {"company": "Turner Construction", "role": "Project Management Intern", "location": "Remote", "url": "https://www.turnerconstruction.com/careers"},
            {"company": "Skanska", "role": "Construction Intern", "location": "Hybrid", "url": "https://www.skanska.com/careers"},
            {"company": "Kiewit", "role": "Field Operations Intern", "location": "On-site", "url": "https://www.kiewit.com/careers"},
        ],
    },
    "Surveying": {
        "courses": [
            {"course": "Land Surveying Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/land-surveying"},
            {"course": "Geomatics Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/geomatics"},
            {"course": "GPS and GNSS Surveying", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/gps-surveying"},
            {"course": "Total Station Surveying", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/surveying"},
            {"course": "Remote Sensing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/surveying"},
        ],
        "internships": [
            {"company": "Trimble", "role": "Surveying Intern", "location": "Remote", "url": "https://www.trimble.com/careers"},
            {"company": "Leica Geosystems", "role": "Geomatics Intern", "location": "Hybrid", "url": "https://leica-geosystems.com/careers"},
            {"company": "Topcon", "role": "Survey Engineering Intern", "location": "On-site", "url": "https://www.topconpositioning.com/careers"},
        ],
    },
    "Project Planning": {
        "courses": [
            {"course": "Project Management Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/project-management-fundamentals"},
            {"course": "Project Planning and Control", "platform": "Coursera", "url": "https://www.coursera.org/learn/project-planning"},
            {"course": "Primavera P6", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/primavera-p6"},
            {"course": "Microsoft Project", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/project-planning"},
            {"course": "Agile Project Management", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/project-planning"},
        ],
        "internships": [
            {"company": "PMI", "role": "Project Management Intern", "location": "Remote", "url": "https://www.pmi.org/careers"},
            {"company": "Oracle", "role": "Project Planning Intern", "location": "Hybrid", "url": "https://www.oracle.com/careers"},
            {"company": "SAP", "role": "Project Management Intern", "location": "On-site", "url": "https://jobs.sap.com"},
        ],
    },
    "Process Design": {
        "courses": [
            {"course": "Chemical Process Design", "platform": "Udemy", "url": "https://www.udemy.com/course/chemical-process-design"},
            {"course": "Process Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/chemical-engineering"},
            {"course": "P&ID Development", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/process-design"},
            {"course": "HYSYS Simulation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/process-design"},
            {"course": "Aspen Plus", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/process-design"},
        ],
        "internships": [
            {"company": "Air Products", "role": "Process Engineering Intern", "location": "Remote", "url": "https://www.airproducts.com/careers"},
            {"company": "Linde", "role": "Process Design Intern", "location": "Hybrid", "url": "https://www.linde.com/careers"},
            {"company": "Praxair", "role": "Chemical Engineering Intern", "location": "On-site", "url": "https://www.praxair.com/careers"},
        ],
    },
    "Heat Transfer": {
        "courses": [
            {"course": "Heat Transfer Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/heat-transfer"},
            {"course": "Thermal Systems Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/thermal-systems"},
            {"course": "CFD for Heat Transfer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cfd-heat-transfer"},
            {"course": "Boiler and Heat Exchanger Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/heat-transfer"},
            {"course": "Radiation Heat Transfer", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/heat-transfer"},
        ],
        "internships": [
            {"company": "Honeywell UOP", "role": "Process Engineering Intern", "location": "Remote", "url": "https://careers.honeywell.com"},
            {"company": "Eastman Chemical", "role": "Chemical Engineering Intern", "location": "Hybrid", "url": "https://www.eastman.com/careers"},
            {"company": "Celanese", "role": "Process Engineering Intern", "location": "On-site", "url": "https://www.celanese.com/careers"},
        ],
    },
    "Chemical Thermodynamics": {
        "courses": [
            {"course": "Chemical Thermodynamics", "platform": "Udemy", "url": "https://www.udemy.com/course/chemical-thermodynamics"},
            {"course": "Thermodynamics for Chemical Engineers", "platform": "Coursera", "url": "https://www.coursera.org/learn/thermodynamics"},
            {"course": "Phase Equilibrium", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/phase-equilibrium"},
            {"course": "Chemical Reaction Thermodynamics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/chemical-engineering"},
            {"course": "Statistical Thermodynamics", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/chemical-engineering"},
        ],
        "internships": [
            {"company": "Dow", "role": "Chemical Engineering Intern", "location": "Remote", "url": "https://www.dow.com/careers"},
            {"company": "DuPont", "role": "R&D Engineering Intern", "location": "Hybrid", "url": "https://www.dupont.com/careers"},
            {"company": "BASF", "role": "Process Engineering Intern", "location": "On-site", "url": "https://www.basf.com/careers"},
        ],
    },
    "Safety": {
        "courses": [
            {"course": "Process Safety Management", "platform": "Udemy", "url": "https://www.udemy.com/course/process-safety-management"},
            {"course": "Hazard and Operability Study", "platform": "Coursera", "url": "https://www.coursera.org/learn/process-safety"},
            {"course": "HAZOP and LOPA", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/hazop-analysis"},
            {"course": "OSHA Standards", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/occupational-safety"},
            {"course": "Risk Assessment", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/safety-management"},
        ],
        "internships": [
            {"company": "BakerRisk", "role": "Safety Engineering Intern", "location": "Remote", "url": "https://www.bakerrisk.com/careers"},
            {"company": "ioMosaic", "role": "Process Safety Intern", "location": "Hybrid", "url": "https://www.iomosaic.com/careers"},
            {"company": "ABS Group", "role": "Safety Consulting Intern", "location": "On-site", "url": "https://www.abs-group.com/careers"},
        ],
    },
    "Reaction Engineering": {
        "courses": [
            {"course": "Chemical Reaction Engineering", "platform": "Udemy", "url": "https://www.udemy.com/course/chemical-reaction-engineering"},
            {"course": "Reactor Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/chemical-reactors"},
            {"course": "Catalysis and Reaction Kinetics", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/reaction-kinetics"},
            {"course": "Biochemical Engineering", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/reaction-engineering"},
            {"course": "Polymer Reaction Engineering", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/reaction-engineering"},
        ],
        "internships": [
            {"company": "Cabot Corporation", "role": "Reaction Engineering Intern", "location": "Remote", "url": "https://www.cabotcorp.com/careers"},
            {"company": "Wacker Chemie", "role": "Chemical Engineering Intern", "location": "Hybrid", "url": "https://www.wacker.com/careers"},
            {"company": "Evonik", "role": "Process Engineering Intern", "location": "On-site", "url": "https://corporate.evonik.com/careers"},
        ],
    },
    "Simulation": {
        "courses": [
            {"course": "Process Simulation", "platform": "Udemy", "url": "https://www.udemy.com/course/process-simulation"},
            {"course": "Aspen Plus Simulation", "platform": "Coursera", "url": "https://www.coursera.org/learn/process-simulation"},
            {"course": "CFD Simulation", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cfd-simulation"},
            {"course": "Discrete Event Simulation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/simulation"},
            {"course": "Monte Carlo Simulation", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/simulation"},
        ],
        "internships": [
            {"company": "ANSYS", "role": "Simulation Engineering Intern", "location": "Remote", "url": "https://www.ansys.com/careers"},
            {"company": "Siemens", "role": "Simulation Intern", "location": "Hybrid", "url": "https://www.sw.siemens.com/careers"},
            {"company": "Altair", "role": "Simulation Engineering Intern", "location": "On-site", "url": "https://www.altair.com/careers"},
        ],
    },
    "Process Improvement": {
        "courses": [
            {"course": "Process Improvement Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/process-improvement"},
            {"course": "Six Sigma Green Belt", "platform": "Coursera", "url": "https://www.coursera.org/specializations/six-sigma-green-belt"},
            {"course": "Kaizen and Continuous Improvement", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/continuous-improvement"},
            {"course": "Value Stream Mapping", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/process-improvement"},
            {"course": "Root Cause Analysis", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/process-improvement"},
        ],
        "internships": [
            {"company": "McKinsey", "role": "Operations Intern", "location": "Remote", "url": "https://www.mckinsey.com/careers"},
            {"company": "Boston Consulting Group", "role": "Process Improvement Intern", "location": "Hybrid", "url": "https://www.bcg.com/careers"},
            {"company": "Bain", "role": "Operations Intern", "location": "On-site", "url": "https://www.bain.com/careers"},
        ],
    },
    "Six Sigma": {
        "courses": [
            {"course": "Six Sigma Yellow Belt", "platform": "Udemy", "url": "https://www.udemy.com/course/six-sigma-yellow-belt"},
            {"course": "Six Sigma Black Belt", "platform": "Coursera", "url": "https://www.coursera.org/specializations/six-sigma-black-belt"},
            {"course": "DMAIC Methodology", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/six-sigma-dmaic"},
            {"course": "Statistical Process Control", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/six-sigma"},
            {"course": "Design for Six Sigma", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/six-sigma"},
        ],
        "internships": [
            {"company": "Motorola Solutions", "role": "Six Sigma Intern", "location": "Remote", "url": "https://www.motorolasolutions.com/careers"},
            {"company": "General Electric", "role": "Quality Engineering Intern", "location": "Hybrid", "url": "https://www.ge.com/careers"},
            {"company": "Honeywell", "role": "Six Sigma Intern", "location": "On-site", "url": "https://careers.honeywell.com"},
        ],
    },
    "Operations Research": {
        "courses": [
            {"course": "Operations Research Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/operations-research"},
            {"course": "Optimization Methods", "platform": "Coursera", "url": "https://www.coursera.org/learn/optimization"},
            {"course": "Linear Programming", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/linear-programming"},
            {"course": "Queueing Theory", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/operations-research"},
            {"course": "Network Optimization", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/operations-research"},
        ],
        "internships": [
            {"company": "Amazon", "role": "Operations Research Intern", "location": "Remote", "url": "https://www.amazon.jobs"},
            {"company": "UPS", "role": "Operations Research Intern", "location": "Hybrid", "url": "https://www.jobs-ups.com"},
            {"company": "FedEx", "role": "Operations Intern", "location": "On-site", "url": "https://careers.fedex.com"},
        ],
    },
    "Supply Chain": {
        "courses": [
            {"course": "Supply Chain Management", "platform": "Udemy", "url": "https://www.udemy.com/course/supply-chain-management"},
            {"course": "Supply Chain Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/supply-chain-management"},
            {"course": "Logistics and Distribution", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/logistics-management"},
            {"course": "Demand Planning", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/supply-chain"},
            {"course": "Inventory Management", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/supply-chain"},
        ],
        "internships": [
            {"company": "DHL", "role": "Supply Chain Intern", "location": "Remote", "url": "https://www.dhl.com/careers"},
            {"company": "Maersk", "role": "Supply Chain Intern", "location": "Hybrid", "url": "https://www.maersk.com/careers"},
            {"company": "C.H. Robinson", "role": "Logistics Intern", "location": "On-site", "url": "https://www.chrobinson.com/careers"},
        ],
    },
    "Quality Control": {
        "courses": [
            {"course": "Quality Control Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/quality-control"},
            {"course": "Statistical Quality Control", "platform": "Coursera", "url": "https://www.coursera.org/learn/quality-control"},
            {"course": "ISO 9001 Quality Management", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/iso-9001"},
            {"course": "SPC and Control Charts", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/quality-control"},
            {"course": "Quality Auditing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/quality-control"},
        ],
        "internships": [
            {"company": "Tesla", "role": "Quality Engineering Intern", "location": "Remote", "url": "https://www.tesla.com/careers"},
            {"company": "Boeing", "role": "Quality Intern", "location": "Hybrid", "url": "https://jobs.boeing.com"},
            {"company": "Toyota", "role": "Quality Control Intern", "location": "On-site", "url": "https://www.toyota.com/careers"},
        ],
    },
    "ERP": {
        "courses": [
            {"course": "SAP ERP Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/sap-erp-fundamentals"},
            {"course": "Oracle ERP Cloud", "platform": "Coursera", "url": "https://www.coursera.org/learn/oracle-erp"},
            {"course": "Microsoft Dynamics 365", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/dynamics-365-fundamentals"},
            {"course": "NetSuite ERP", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/erp"},
            {"course": "Workday HCM", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/erp"},
        ],
        "internships": [
            {"company": "SAP", "role": "ERP Consulting Intern", "location": "Remote", "url": "https://jobs.sap.com"},
            {"company": "Oracle", "role": "ERP Implementation Intern", "location": "Hybrid", "url": "https://www.oracle.com/careers"},
            {"company": "Microsoft", "role": "Dynamics 365 Intern", "location": "On-site", "url": "https://careers.microsoft.com"},
        ],
    },
    "Production Planning": {
        "courses": [
            {"course": "Production Planning and Control", "platform": "Udemy", "url": "https://www.udemy.com/course/production-planning"},
            {"course": "Manufacturing Planning", "platform": "Coursera", "url": "https://www.coursera.org/learn/manufacturing-planning"},
            {"course": "MRP and ERP Planning", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/mrp-planning"},
            {"course": "Advanced Planning and Scheduling", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/production-planning"},
            {"course": "Just-in-Time Manufacturing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/production-planning"},
        ],
        "internships": [
            {"company": "Plex Systems", "role": "Production Planning Intern", "location": "Remote", "url": "https://www.plex.com/careers"},
            {"company": "Epicor", "role": "ERP Intern", "location": "Hybrid", "url": "https://www.epicor.com/careers"},
            {"company": "Infor", "role": "Manufacturing Intern", "location": "On-site", "url": "https://www.infor.com/careers"},
        ],
    },
    "Biomaterials": {
        "courses": [
            {"course": "Biomaterials Science", "platform": "Udemy", "url": "https://www.udemy.com/course/biomaterials"},
            {"course": "Introduction to Biomaterials", "platform": "Coursera", "url": "https://www.coursera.org/learn/biomaterials"},
            {"course": "Tissue Engineering", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/tissue-engineering"},
            {"course": "Biocompatibility Testing", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/biomaterials"},
            {"course": "Implant Materials", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/biomaterials"},
        ],
        "internships": [
            {"company": "Medtronic", "role": "Biomaterials Intern", "location": "Remote", "url": "https://www.medtronic.com/careers"},
            {"company": "Johnson & Johnson", "role": "Materials Science Intern", "location": "Hybrid", "url": "https://www.jnj.com/careers"},
            {"company": "Stryker", "role": "Biomedical Engineering Intern", "location": "On-site", "url": "https://careers.stryker.com"},
        ],
    },
    "Medical Imaging": {
        "courses": [
            {"course": "Medical Imaging Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/medical-imaging"},
            {"course": "MRI and CT Physics", "platform": "Coursera", "url": "https://www.coursera.org/learn/medical-imaging"},
            {"course": "Radiology Informatics", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/radiology-informatics"},
            {"course": "DICOM Standards", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/medical-imaging"},
            {"course": "Image-Guided Surgery", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/medical-imaging"},
        ],
        "internships": [
            {"company": "GE HealthCare", "role": "Imaging Engineering Intern", "location": "Remote", "url": "https://www.gehealthcare.com/careers"},
            {"company": "Siemens Healthineers", "role": "Medical Imaging Intern", "location": "Hybrid", "url": "https://www.siemens-healthineers.com/careers"},
            {"company": "Philips Healthcare", "role": "Imaging Intern", "location": "On-site", "url": "https://www.philips.com/careers"},
        ],
    },
    "Biomechanics": {
        "courses": [
            {"course": "Biomechanics Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/biomechanics"},
            {"course": "Musculoskeletal Biomechanics", "platform": "Coursera", "url": "https://www.coursera.org/learn/biomechanics"},
            {"course": "Motion Capture Analysis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/motion-capture"},
            {"course": "Gait Analysis", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/biomechanics"},
            {"course": "Orthopedic Biomechanics", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/biomechanics"},
        ],
        "internships": [
            {"company": "Zimmer Biomet", "role": "Biomechanics Intern", "location": "Remote", "url": "https://www.zimmerbiomet.com/careers"},
            {"company": "DePuy Synthes", "role": "Engineering Intern", "location": "Hybrid", "url": "https://www.depuysynthes.com/careers"},
            {"company": "Smith & Nephew", "role": "R&D Intern", "location": "On-site", "url": "https://www.smith-nephew.com/careers"},
        ],
    },
    "Regulatory Standards": {
        "courses": [
            {"course": "FDA Regulations for Medical Devices", "platform": "Udemy", "url": "https://www.udemy.com/course/fda-regulations"},
            {"course": "ISO 13485 Quality Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/iso-13485"},
            {"course": "CE Marking for Medical Devices", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ce-marking"},
            {"course": "21 CFR Part 820", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/regulatory-affairs"},
            {"course": "Clinical Trial Regulations", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/regulatory-affairs"},
        ],
        "internships": [
            {"company": "FDA", "role": "Regulatory Intern", "location": "Remote", "url": "https://www.fda.gov/jobs"},
            {"company": "Emergo by UL", "role": "Regulatory Affairs Intern", "location": "Hybrid", "url": "https://www.emergogroup.com/careers"},
            {"company": "NAMSA", "role": "Regulatory Consulting Intern", "location": "On-site", "url": "https://www.namsa.com/careers"},
        ],
    },
    "Robotics": {
        "courses": [
            {"course": "Robotics Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/robotics"},
            {"course": "Modern Robotics", "platform": "Udemy", "url": "https://www.udemy.com/course/modern-robotics"},
            {"course": "Robot Operating System (ROS)", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ros-fundamentals"},
            {"course": "Robotic Manipulators", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/robotics"},
            {"course": "Autonomous Robotics", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/robotics"},
        ],
        "internships": [
            {"company": "Boston Dynamics", "role": "Robotics Engineering Intern", "location": "Remote", "url": "https://www.bostondynamics.com/careers"},
            {"company": "iRobot", "role": "Robotics Intern", "location": "Hybrid", "url": "https://www.irobot.com/careers"},
            {"company": "Universal Robots", "role": "Robotics Engineering Intern", "location": "On-site", "url": "https://www.universal-robots.com/careers"},
        ],
    },
    "ROS": {
        "courses": [
            {"course": "ROS for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/ros-for-beginners"},
            {"course": "ROS Navigation Stack", "platform": "Coursera", "url": "https://www.coursera.org/learn/ros-navigation"},
            {"course": "ROS2 Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/ros2-fundamentals"},
            {"course": "Gazebo Simulation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/ros"},
            {"course": "MoveIt Motion Planning", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/ros"},
        ],
        "internships": [
            {"company": "Open Robotics", "role": "ROS Engineering Intern", "location": "Remote", "url": "https://www.openrobotics.org/careers"},
            {"company": "Fetch Robotics", "role": "Robotics Intern", "location": "Hybrid", "url": "https://www.fetchrobotics.com/careers"},
            {"company": "Locus Robotics", "role": "Robotics Engineering Intern", "location": "On-site", "url": "https://locusrobotics.com/careers"},
        ],
    },
    "Sensors": {
        "courses": [
            {"course": "Sensor Technology", "platform": "Udemy", "url": "https://www.udemy.com/course/sensor-technology"},
            {"course": "IoT Sensors and Actuators", "platform": "Coursera", "url": "https://www.coursera.org/learn/iot-sensors"},
            {"course": "MEMS and NEMS", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/mems-sensors"},
            {"course": "Wearable Sensors", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/sensors"},
            {"course": "Sensor Fusion", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/sensors"},
        ],
        "internships": [
            {"company": "Bosch Sensortec", "role": "Sensor Engineering Intern", "location": "Remote", "url": "https://www.bosch-sensortec.com/careers"},
            {"company": "TE Connectivity", "role": "Sensor Intern", "location": "Hybrid", "url": "https://www.te.com/careers"},
            {"company": "Amphenol", "role": "Sensor Engineering Intern", "location": "On-site", "url": "https://www.amphenol.com/careers"},
        ],
    },
    "Actuators": {
        "courses": [
            {"course": "Actuator Design", "platform": "Udemy", "url": "https://www.udemy.com/course/actuator-design"},
            {"course": "Electric Drives", "platform": "Coursera", "url": "https://www.coursera.org/learn/electric-drives"},
            {"course": "Hydraulic and Pneumatic Systems", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/hydraulic-systems"},
            {"course": "Servo Motor Control", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/actuators"},
            {"course": "Piezoelectric Actuators", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/actuators"},
        ],
        "internships": [
            {"company": "Parker Hannifin", "role": "Actuator Engineering Intern", "location": "Remote", "url": "https://www.parker.com/careers"},
            {"company": "Moog", "role": "Motion Control Intern", "location": "Hybrid", "url": "https://www.moog.com/careers"},
            {"company": "SMC Corporation", "role": "Actuator Engineering Intern", "location": "On-site", "url": "https://www.smcworld.com/careers"},
        ],
    },
    "Kinematics": {
        "courses": [
            {"course": "Robot Kinematics", "platform": "Udemy", "url": "https://www.udemy.com/course/robot-kinematics"},
            {"course": "Forward and Inverse Kinematics", "platform": "Coursera", "url": "https://www.coursera.org/learn/robot-kinematics"},
            {"course": "Spatial Kinematics", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/robot-kinematics"},
            {"course": "Jacobian and Dynamics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/robotics"},
            {"course": "Trajectory Planning", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/robotics"},
        ],
        "internships": [
            {"company": "ABB Robotics", "role": "Robotics Engineering Intern", "location": "Remote", "url": "https://new.abb.com/careers"},
            {"company": "KUKA", "role": "Robotics Intern", "location": "Hybrid", "url": "https://www.kuka.com/careers"},
            {"company": "FANUC", "role": "Robotics Engineering Intern", "location": "On-site", "url": "https://www.fanucamerica.com/careers"},
        ],
    },
    "Connectivity": {
        "courses": [
            {"course": "IoT Connectivity Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/iot-connectivity"},
            {"course": "Wireless Communication for IoT", "platform": "Coursera", "url": "https://www.coursera.org/learn/iot-connectivity"},
            {"course": "5G and IoT", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/5g-iot"},
            {"course": "LPWAN Technologies", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/iot-connectivity"},
            {"course": "Bluetooth and Zigbee", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/iot-connectivity"},
        ],
        "internships": [
            {"company": "Sierra Wireless", "role": "IoT Connectivity Intern", "location": "Remote", "url": "https://www.sierrawireless.com/careers"},
            {"company": "Telit", "role": "IoT Engineering Intern", "location": "Hybrid", "url": "https://www.telit.com/careers"},
            {"company": "u-blox", "role": "Connectivity Engineering Intern", "location": "On-site", "url": "https://www.u-blox.com/careers"},
        ],
    },
    "MQTT": {
        "courses": [
            {"course": "MQTT Protocol Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/mqtt-protocol"},
            {"course": "IoT Messaging with MQTT", "platform": "Coursera", "url": "https://www.coursera.org/learn/mqtt-iot"},
            {"course": "MQTT Broker Setup", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/mqtt-fundamentals"},
            {"course": "MQTT Security", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/mqtt"},
            {"course": "MQTT and AWS IoT", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/mqtt"},
        ],
        "internships": [
            {"company": "HiveMQ", "role": "IoT Engineering Intern", "location": "Remote", "url": "https://www.hivemq.com/careers"},
            {"company": "Eclipse Foundation", "role": "Open Source Intern", "location": "Hybrid", "url": "https://www.eclipse.org/careers"},
            {"company": "EMQ", "role": "MQTT Engineering Intern", "location": "On-site", "url": "https://www.emqx.io/careers"},
        ],
    },
    "Cloud Platforms": {
        "courses": [
            {"course": "AWS IoT Core", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-iot-core"},
            {"course": "Azure IoT Hub", "platform": "Coursera", "url": "https://www.coursera.org/learn/azure-iot"},
            {"course": "Google Cloud IoT", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/google-cloud-iot"},
            {"course": "IBM Watson IoT", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/iot-cloud"},
            {"course": "Particle IoT Platform", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/iot-cloud"},
        ],
        "internships": [
            {"company": "Particle", "role": "IoT Platform Intern", "location": "Remote", "url": "https://www.particle.io/careers"},
            {"company": "Blynk", "role": "IoT Engineering Intern", "location": "Hybrid", "url": "https://blynk.io/careers"},
            {"company": "ThingWorx", "role": "IoT Development Intern", "location": "On-site", "url": "https://www.ptc.com/careers"},
        ],
    },
    "Data Analytics": {
        "courses": [
            {"course": "IoT Data Analytics", "platform": "Udemy", "url": "https://www.udemy.com/course/iot-data-analytics"},
            {"course": "Big Data for IoT", "platform": "Coursera", "url": "https://www.coursera.org/learn/iot-data-analytics"},
            {"course": "Time Series Analysis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/time-series-analysis"},
            {"course": "Edge Analytics", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/iot-analytics"},
            {"course": "Real-Time Data Processing", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/iot-analytics"},
        ],
        "internships": [
            {"company": "Splunk", "role": "IoT Analytics Intern", "location": "Remote", "url": "https://www.splunk.com/careers"},
            {"company": "Cloudera", "role": "Data Engineering Intern", "location": "Hybrid", "url": "https://www.cloudera.com/careers"},
            {"company": "Databricks", "role": "IoT Data Intern", "location": "On-site", "url": "https://www.databricks.com/company/careers"},
        ],
    },
}
