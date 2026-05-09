import json

# All skills data as a Python dict
skills = {}

# Helper to add skill
def add_skill(name, courses, internships):
    skills[name] = {"courses": courses, "internships": internships}

# Programming Languages
add_skill("Python", [
    {"course": "Python for Everybody Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python"},
    {"course": "Complete Python Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-python-bootcamp"},
    {"course": "Python 3 Programming Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python-3-programming"},
    {"course": "Python Data Structures", "platform": "edX", "url": "https://www.edx.org/learn/python/python-basics-for-data-science"},
    {"course": "Advanced Python", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/advanced-python"},
], [
    {"company": "Google", "role": "Python Developer Intern", "location": "Remote", "url": "https://careers.google.com"},
    {"company": "Microsoft", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://careers.microsoft.com"},
    {"company": "Amazon", "role": "Backend Engineer Intern", "location": "On-site", "url": "https://www.amazon.jobs"},
])

add_skill("Java", [
    {"course": "Java Programming and Software Engineering Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/java-programming"},
    {"course": "Java Programming Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/java-the-complete-java-developer-course"},
    {"course": "Object Oriented Programming in Java", "platform": "edX", "url": "https://www.edx.org/learn/java/object-oriented-programming-in-java"},
    {"course": "Java SE 11 Developer Certification", "platform": "Pluralsight", "url": "https://www.pluralsight.com/paths/java-se-11-developer-certification-1z0-819"},
    {"course": "Java Enterprise Edition", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/java-enterprise"},
], [
    {"company": "Oracle", "role": "Java Developer Intern", "location": "Remote", "url": "https://www.oracle.com/careers"},
    {"company": "IBM", "role": "Software Engineer Intern", "location": "Hybrid", "url": "https://www.ibm.com/careers"},
    {"company": "SAP", "role": "Java Backend Intern", "location": "On-site", "url": "https://jobs.sap.com"},
])

add_skill("C++", [
    {"course": "C++ For C Programmers", "platform": "Coursera", "url": "https://www.coursera.org/learn/c-plus-plus-a"},
    {"course": "Beginning C++ Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/beginning-c-plus-plus-programming"},
    {"course": "Introduction to C++", "platform": "edX", "url": "https://www.edx.org/learn/c/microsoft-introduction-to-c"},
    {"course": "C++ Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/cpp-fundamentals"},
    {"course": "Modern C++ Concurrency", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/c-plus-plus"},
], [
    {"company": "NVIDIA", "role": "C++ Software Intern", "location": "Remote", "url": "https://www.nvidia.com/en-us/about-nvidia/careers"},
    {"company": "Bloomberg", "role": "Software Engineering Intern", "location": "On-site", "url": "https://www.bloomberg.com/company/careers"},
    {"company": "Adobe", "role": "C++ Developer Intern", "location": "Hybrid", "https://careers.adobe.com"},
])

add_skill("C", [
    {"course": "C Programming: Getting Started", "platform": "edX", "url": "https://www.edx.org/learn/c/dartmouth-c-programming-getting-started"},
    {"course": "C Programming For Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/c-programming-for-beginners"},
    {"course": "C for Everyone: Programming Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/c-for-everyone"},
    {"course": "Advanced C Programming", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/c"},
    {"course": "Embedded C Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/embedded-c-programming"},
], [
    {"company": "Intel", "role": "Firmware Engineering Intern", "location": "On-site", "url": "https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"},
    {"company": "Texas Instruments", "role": "Embedded Software Intern", "location": "Hybrid", "url": "https://careers.ti.com"},
    {"company": "Qualcomm", "role": "Embedded Systems Intern", "location": "On-site", "url": "https://www.qualcomm.com/company/careers"},
])

add_skill("R", [
    {"course": "R Programming", "platform": "Coursera", "url": "https://www.coursera.org/learn/r-programming"},
    {"course": "Data Science with R", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/data-scientist-with-r"},
    {"course": "R for Data Science", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/r-data-science"},
    {"course": "Advanced R Programming", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/r"},
    {"course": "Statistics with R", "platform": "edX", "url": "https://www.edx.org/learn/r/statistics"},
], [
    {"company": "RStudio", "role": "Data Science Intern", "location": "Remote", "url": "https://posit.co/careers"},
    {"company": "Biogen", "role": "Biostatistics Intern", "location": "Hybrid", "url": "https://www.biogen.com/careers"},
    {"company": "Pfizer", "role": "R Programming Intern", "location": "On-site", "url": "https://www.pfizer.com/careers"},
])

add_skill("JavaScript", [
    {"course": "JavaScript: The Advanced Concepts", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-javascript-concepts"},
    {"course": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures"},
    {"course": "Modern JavaScript from the Beginning", "platform": "Udemy", "url": "https://www.udemy.com/course/modern-javascript-from-the-beginning"},
    {"course": "JavaScript Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/javascript"},
    {"course": "ES6 JavaScript: The Complete Developer", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/javascript-es6"},
], [
    {"company": "Netflix", "role": "JavaScript Engineering Intern", "location": "Remote", "url": "https://jobs.netflix.com"},
    {"company": "Uber", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.uber.com/careers"},
    {"company": "Airbnb", "role": "Web Platform Intern", "location": "On-site", "url": "https://careers.airbnb.com"},
])

add_skill("Node.js", [
    {"course": "Node.js, Express, MongoDB Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp"},
    {"course": "Server-side Development with NodeJS", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
    {"course": "Node.js Microservices", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/node-js-microservices"},
    {"course": "Advanced Node.js", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/node-js"},
    {"course": "Node.js Design Patterns", "platform": "Udemy", "url": "https://www.udemy.com/course/nodejs-design-patterns"},
], [
    {"company": "PayPal", "role": "Node.js Developer Intern", "location": "Remote", "url": "https://www.paypal.com/us/webapps/mpp/jobs"},
    {"company": "Slack", "role": "Backend Engineering Intern", "location": "Hybrid", "url": "https://slack.com/careers"},
    {"company": "Medium", "role": "Platform Engineering Intern", "location": "On-site", "url": "https://medium.com/jobs"},
])

add_skill("TypeScript", [
    {"course": "Understanding TypeScript", "platform": "Udemy", "url": "https://www.udemy.com/course/understanding-typescript"},
    {"course": "TypeScript Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/typescript-fundamentals"},
    {"course": "TypeScript: The Complete Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/typescript-the-complete-developers-guide"},
    {"course": "Advanced TypeScript", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/typescript"},
    {"course": "TypeScript with React", "platform": "Coursera", "url": "https://www.coursera.org/learn/typescript"},
], [
    {"company": "Linear", "role": "TypeScript Engineering Intern", "location": "Remote", "url": "https://linear.app/careers"},
    {"company": "Notion", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.notion.so/careers"},
    {"company": "Figma", "role": "Web Engineering Intern", "location": "On-site", "url": "https://www.figma.com/careers"},
])

# Fundamentals
add_skill("Data Structures", [
    {"course": "Data Structures and Algorithms Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/data-structures-algorithms"},
    {"course": "Master the Coding Interview", "platform": "Udemy", "url": "https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms"},
    {"course": "Data Structures Fundamentals", "platform": "edX", "url": "https://www.edx.org/learn/data-structures"},
    {"course": "Algorithms and Data Structures in Python", "platform": "Udemy", "url": "https://www.udemy.com/course/algorithms-and-data-structures-in-python"},
    {"course": "Data Structures in Java", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/data-structures"},
], [
    {"company": "Meta", "role": "Software Engineering Intern", "location": "Remote", "url": "https://www.metacareers.com"},
    {"company": "Apple", "role": "Algorithms Engineer Intern", "location": "On-site", "url": "https://jobs.apple.com"},
    {"company": "LinkedIn", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://careers.linkedin.com"},
])

add_skill("Algorithms", [
    {"course": "Algorithmic Toolbox", "platform": "Coursera", "url": "https://www.coursera.org/learn/algorithmic-toolbox"},
    {"course": "Algorithms Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/algorithms"},
    {"course": "Grokking the Coding Interview", "platform": "Educative", "url": "https://www.educative.io/courses/grokking-the-coding-interview"},
    {"course": "Introduction to Algorithms", "platform": "MIT OpenCourseWare", "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011"},
    {"course": "Competitive Programming", "platform": "Codeforces", "url": "https://codeforces.com/edu/course/2"},
], [
    {"company": "Two Sigma", "role": "Quantitative Research Intern", "location": "On-site", "url": "https://www.twosigma.com/careers"},
    {"company": "Jane Street", "role": "Software Engineering Intern", "location": "Hybrid", "url": "https://www.janestreet.com/join-jane-street"},
    {"company": "Citadel", "role": "Algorithm Engineering Intern", "location": "On-site", "url": "https://www.citadel.com/careers"},
])

add_skill("OOP", [
    {"course": "Object-Oriented Programming in Java", "platform": "Coursera", "url": "https://www.coursera.org/learn/object-oriented-java"},
    {"course": "OOP in Python", "platform": "Udemy", "url": "https://www.udemy.com/course/object-oriented-programming-python"},
    {"course": "Design Patterns in OOP", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/design-patterns-overview"},
    {"course": "SOLID Principles", "platform": "Coursera", "url": "https://www.coursera.org/learn/solid-principles-object-oriented-design"},
    {"course": "OOP Design Patterns", "platform": "edX", "url": "https://www.edx.org/learn/object-oriented-programming"},
], [
    {"company": "Salesforce", "role": "Software Engineering Intern", "location": "Remote", "url": "https://careers.salesforce.com"},
    {"company": "Oracle", "role": "Java OOP Developer Intern", "location": "Hybrid", "url": "https://www.oracle.com/careers"},
    {"company": "Intuit", "role": "Software Engineering Intern", "location": "On-site", "url": "https://www.intuit.com/careers"},
])

add_skill("Git", [
    {"course": "Git and GitHub Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/google-it-automation"},
    {"course": "Git Complete: The Definitive Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/git-complete"},
    {"course": "GitHub Actions", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/github"},
    {"course": "Advanced Git", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/advanced-git"},
    {"course": "Git Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-git"},
], [
    {"company": "GitHub", "role": "Software Engineering Intern", "location": "Remote", "url": "https://github.com/about/careers"},
    {"company": "GitLab", "role": "Engineering Intern", "location": "Remote", "url": "https://about.gitlab.com/jobs"},
    {"company": "Atlassian", "role": "DevOps Intern", "location": "Hybrid", "url": "https://www.atlassian.com/company/careers"},
])

add_skill("SQL", [
    {"course": "SQL for Data Science", "platform": "Coursera", "url": "https://www.coursera.org/learn/sql-for-data-science"},
    {"course": "The Complete SQL Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-sql-bootcamp"},
    {"course": "Introduction to SQL", "platform": "edX", "url": "https://www.edx.org/learn/sql"},
    {"course": "Advanced SQL", "platform": "DataCamp", "url": "https://www.datacamp.com/courses/advanced-sql"},
    {"course": "SQL Querying", "platform": "Khan Academy", "url": "https://www.khanacademy.org/computing/computer-programming/sql"},
], [
    {"company": "Snowflake", "role": "Data Engineering Intern", "location": "Remote", "url": "https://careers.snowflake.com"},
    {"company": "Databricks", "role": "SQL Analytics Intern", "location": "Hybrid", "url": "https://www.databricks.com/company/careers"},
    {"company": "MongoDB", "role": "Database Engineering Intern", "location": "On-site", "url": "https://www.mongodb.com/careers"},
])

add_skill("Linux", [
    {"course": "Linux Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/linux-fundamentals"},
    {"course": "Linux Administration Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/linux-administration-bootcamp"},
    {"course": "Introduction to Linux", "platform": "edX", "url": "https://www.edx.org/learn/linux"},
    {"course": "Linux Command Line Basics", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-the-command-line"},
    {"course": "Red Hat Certified System Administrator", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/red-hat-system-administrator"},
], [
    {"company": "Red Hat", "role": "Linux Engineering Intern", "location": "Remote", "url": "https://www.redhat.com/en/jobs"},
    {"company": "Canonical", "role": "Ubuntu Engineering Intern", "location": "Remote", "url": "https://canonical.com/careers"},
    {"company": "SUSE", "role": "Systems Engineering Intern", "location": "Hybrid", "url": "https://www.suse.com/careers"},
])

add_skill("REST APIs", [
    {"course": "APIs and Microservices", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/apis-and-microservices"},
    {"course": "REST API Design", "platform": "Udemy", "url": "https://www.udemy.com/course/rest-api-design"},
    {"course": "Building RESTful APIs with Node.js", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
    {"course": "API Testing with Postman", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/api"},
    {"course": "GraphQL and REST API Design", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/designing-restful-web-apis"},
], [
    {"company": "Stripe", "role": "API Engineering Intern", "location": "Remote", "url": "https://stripe.com/jobs"},
    {"company": "Twilio", "role": "Developer Relations Intern", "location": "Hybrid", "url": "https://www.twilio.com/company/jobs"},
    {"company": "SendGrid", "role": "API Developer Intern", "location": "On-site", "url": "https://sendgrid.com/careers"},
])

add_skill("RESTful APIs", [
    {"course": "REST API Design, Development", "platform": "Udemy", "url": "https://www.udemy.com/course/rest-api-design"},
    {"course": "APIs and Microservices", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/apis-and-microservices"},
    {"course": "Web Services and APIs", "platform": "Coursera", "url": "https://www.coursera.org/learn/server-side-nodejs"},
    {"course": "Building REST APIs with Django", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/api"},
    {"course": "REST API with Spring Boot", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/rest-api-spring-boot"},
], [
    {"company": "Stripe", "role": "API Engineering Intern", "location": "Remote", "url": "https://stripe.com/jobs"},
    {"company": "Postman", "role": "API Platform Intern", "location": "Hybrid", "url": "https://www.postman.com/careers"},
    {"company": "RapidAPI", "role": "Developer Experience Intern", "location": "On-site", "url": "https://rapidapi.com/careers"},
])

add_skill("Testing", [
    {"course": "Software Testing and Automation", "platform": "Coursera", "url": "https://www.coursera.org/specializations/software-testing-automation"},
    {"course": "Automation Testing with Selenium", "platform": "Udemy", "url": "https://www.udemy.com/course/selenium-webdriver-with-java"},
    {"course": "Test-Driven Development", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/test-driven-development-big-picture"},
    {"course": "Software Testing Fundamentals", "platform": "edX", "url": "https://www.edx.org/learn/software-testing"},
    {"course": "Playwright Test Automation", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/playwright"},
], [
    {"company": "BrowserStack", "role": "QA Engineering Intern", "location": "Remote", "url": "https://www.browserstack.com/careers"},
    {"company": "Sauce Labs", "role": "Test Automation Intern", "location": "Hybrid", "url": "https://saucelabs.com/company/careers"},
    {"company": "Applitools", "role": "Visual AI Testing Intern", "location": "On-site", "url": "https://applitools.com/careers"},
])

add_skill("CI/CD", [
    {"course": "DevOps, CI/CD", "platform": "Coursera", "url": "https://www.coursera.org/learn/introduction-to-devops"},
    {"course": "Jenkins, From Zero to Hero", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero"},
    {"course": "GitHub Actions for CI/CD", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/github-actions"},
    {"course": "Azure DevOps Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/azure-devops-getting-started"},
    {"course": "CI/CD with GitLab", "platform": "Udemy", "url": "https://www.udemy.com/course/gitlab-ci-pipelines"},
], [
    {"company": "CircleCI", "role": "Developer Experience Intern", "location": "Remote", "url": "https://circleci.com/careers"},
    {"company": "GitLab", "role": "CI/CD Engineering Intern", "location": "Remote", "url": "https://about.gitlab.com/jobs"},
    {"company": "Travis CI", "role": "DevOps Engineering Intern", "location": "Hybrid", "url": "https://www.travis-ci.com/careers"},
])

add_skill("Deployment", [
    {"course": "Deploying Applications with Kubernetes", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/deploying-applications-kubernetes"},
    {"course": "AWS Deployment Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-deployment"},
    {"course": "Heroku Deployment Mastery", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/heroku"},
    {"course": "Docker Deployment", "platform": "Coursera", "url": "https://www.coursera.org/learn/deploying-apps-with-docker"},
    {"course": "Vercel and Netlify Deployment", "platform": "Udemy", "url": "https://www.udemy.com/course/deployment-vercel-netlify"},
], [
    {"company": "Vercel", "role": "Platform Engineering Intern", "location": "Remote", "url": "https://vercel.com/careers"},
    {"company": "Heroku", "role": "Infrastructure Intern", "location": "Hybrid", "url": "https://www.heroku.com/careers"},
    {"company": "DigitalOcean", "role": "Cloud Engineering Intern", "location": "On-site", "url": "https://www.digitalocean.com/careers"},
])

add_skill("Caching", [
    {"course": "Redis Caching Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/redis-caching"},
    {"course": "System Design: Caching Strategies", "platform": "Educative", "url": "https://www.educative.io/courses/grokking-system-design"},
    {"course": "Memcached and Redis", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/redis-fundamentals"},
    {"course": "CDN and Edge Caching", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/caching"},
    {"course": "High Performance Caching", "platform": "Coursera", "url": "https://www.coursera.org/learn/scalable-software-architecture"},
], [
    {"company": "Redis", "role": "Software Engineering Intern", "location": "Remote", "url": "https://redis.com/careers"},
    {"company": "Cloudflare", "role": "Edge Computing Intern", "location": "Hybrid", "url": "https://www.cloudflare.com/careers"},
    {"company": "Fastly", "role": "Caching Infrastructure Intern", "location": "On-site", "url": "https://www.fastly.com/careers"},
])

add_skill("Authentication", [
    {"course": "OAuth 2.0 and OpenID Connect", "platform": "Udemy", "url": "https://www.udemy.com/course/oauth-2-and-openid-connect"},
    {"course": "Authentication and Authorization", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/authentication-authorization-asp-dot-net-core"},
    {"course": "JSON Web Tokens (JWT)", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/authentication"},
    {"course": "Identity and Access Management", "platform": "Coursera", "url": "https://www.coursera.org/learn/identity-and-access-management"},
    {"course": "SSO and SAML", "platform": "Udemy", "url": "https://www.udemy.com/course/saml-sso"},
], [
    {"company": "Okta", "role": "Identity Engineering Intern", "location": "Remote", "url": "https://www.okta.com/company/careers"},
    {"company": "Auth0", "role": "Security Engineering Intern", "location": "Hybrid", "url": "https://auth0.com/careers"},
    {"company": "Ping Identity", "role": "IAM Engineering Intern", "location": "On-site", "url": "https://www.pingidentity.com/en/company/careers"},
])

add_skill("Databases", [
    {"course": "Database Systems Concepts", "platform": "Coursera", "url": "https://www.coursera.org/learn/database-systems"},
    {"course": "MongoDB Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/mongodb-the-complete-developers-guide"},
    {"course": "PostgreSQL Advanced", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/postgresql-fundamentals"},
    {"course": "Database Design", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/database-management"},
    {"course": "NoSQL Database Essentials", "platform": "edX", "url": "https://www.edx.org/learn/nosql-databases"},
], [
    {"company": "MongoDB", "role": "Database Engineering Intern", "location": "Remote", "url": "https://www.mongodb.com/careers"},
    {"company": "Cockroach Labs", "role": "Distributed Systems Intern", "location": "Hybrid", "url": "https://www.cockroachlabs.com/careers"},
    {"company": "Neo4j", "role": "Graph Database Intern", "location": "On-site", "url": "https://neo4j.com/careers"},
])

add_skill("Microservices", [
    {"course": "Microservices with Spring Boot", "platform": "Udemy", "url": "https://www.udemy.com/course/microservices-with-spring-boot-and-spring-cloud"},
    {"course": "Building Microservices", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/building-microservices"},
    {"course": "Microservices Architecture", "platform": "Coursera", "url": "https://www.coursera.org/learn/microservices"},
    {"course": "AWS Microservices", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/microservices"},
    {"course": "Microservices Patterns", "platform": "edX", "url": "https://www.edx.org/learn/microservices"},
], [
    {"company": "Netflix", "role": "Microservices Engineering Intern", "location": "Remote", "url": "https://jobs.netflix.com"},
    {"company": "Uber", "role": "Platform Engineering Intern", "location": "Hybrid", "url": "https://www.uber.com/careers"},
    {"company": "Lyft", "role": "Distributed Systems Intern", "location": "On-site", "url": "https://www.lyft.com/careers"},
])

# Web Development
add_skill("HTML", [
    {"course": "HTML and CSS Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-html"},
    {"course": "HTML5 from Scratch", "platform": "Udemy", "url": "https://www.udemy.com/course/html5-from-scratch"},
    {"course": "Web Design for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/web-design"},
    {"course": "HTML Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/html"},
    {"course": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design"},
], [
    {"company": "Vercel", "role": "Frontend Engineering Intern", "location": "Remote", "url": "https://vercel.com/careers"},
    {"company": "Shopify", "role": "Web Developer Intern", "location": "Hybrid", "url": "https://www.shopify.com/careers"},
    {"company": "Wix", "role": "Web Platform Intern", "location": "On-site", "url": "https://www.wix.com/jobs"},
])

add_skill("CSS", [
    {"course": "Advanced CSS and Sass", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-css-and-sass"},
    {"course": "CSS Grid and Flexbox", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/css"},
    {"course": "Modern CSS", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/modern-css"},
    {"course": "CSS Animation Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/css-animation"},
    {"course": "Tailwind CSS Fundamentals", "platform": "Codecademy", "url": "https://www.codecademy.com/learn/learn-tailwind-css"},
], [
    {"company": "Figma", "role": "Design Engineering Intern", "location": "Remote", "url": "https://www.figma.com/careers"},
    {"company": "Canva", "role": "Frontend Engineering Intern", "location": "Hybrid", "url": "https://www.canva.com/careers"},
    {"company": "Webflow", "role": "Web Design Intern", "location": "On-site", "url": "https://webflow.com/careers"},
])

add_skill("React", [
    {"course": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux"},
    {"course": "Front-End Web Development with React", "platform": "Coursera", "url": "https://www.coursera.org/learn/front-end-react"},
    {"course": "React.js Essential Training", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning/topics/react-js"},
    {"course": "Advanced React Patterns", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/reactjs-advanced"},
    {"course": "React Native: Advanced Concepts", "platform": "Udemy", "url": "https://www.udemy.com/course/react-native-advanced"},
], [
    {"company": "Meta", "role": "React Engineering Intern", "location": "Remote", "url": "https://www.metacareers.com"},
    {"company": "Vercel", "role": "Next.js Engineering Intern", "location": "Hybrid", "url": "https://vercel.com/careers"},
    {"company": "Discord", "role": "Frontend Engineering Intern", "location": "On-site", "url": "https://discord.com/careers"},
])

add_skill("
