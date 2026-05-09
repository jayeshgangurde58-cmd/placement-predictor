#!/usr/bin/env python3
import json, os

OUT = "backend/services/course_database.py"

def write_skill(name, courses, internships):
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(f'    "{name}": {{\n')
        f.write('        "courses": [\n')
        for c in courses:
            f.write(f'            {{"course": "{c[0]}", "platform": "{c[1]}", "url": "{c[2]}"}},\n')
        f.write('        ],\n')
        f.write('        "internships": [\n')
        for i in internships:
            f.write(f'            {{"company": "{i[0]}", "role": "{i[1]}", "location": "{i[2]}", "url": "{i[3]}"}},\n')
        f.write('        ],\n')
        f.write('    },\n')

# Init file
with open(OUT, "w", encoding="utf-8") as f:
    f.write('"""Comprehensive course and internship database for all job role skills."""\n\n')
    f.write('from typing import Dict, List, Any\n\n')
    f.write('COURSE_DATABASE: Dict[str, Dict[str, Any]] = {\n')

# Programming Languages
write_skill("Python",
    [("Python for Everybody Specialization","Coursera","https://www.coursera.org/specializations/python"),
     ("Complete Python Bootcamp","Udemy","https://www.udemy.com/course/complete-python-bootcamp"),
     ("Python 3 Programming Specialization","Coursera","https://www.coursera.org/specializations/python-3-programming"),
     ("Python Data Structures","edX","https://www.edx.org/learn/python/python-basics-for-data-science"),
     ("Advanced Python","Pluralsight","https://www.pluralsight.com/courses/advanced-python")],
    [("Google","Python Developer Intern","Remote","https://careers.google.com"),
     ("Microsoft","Software Engineering Intern","Hybrid","https://careers.microsoft.com"),
     ("Amazon","Backend Engineer Intern","On-site","https://www.amazon.jobs")])

write_skill("Java",
    [("Java Programming and Software Engineering Fundamentals","Coursera","https://www.coursera.org/specializations/java-programming"),
     ("Java Programming Masterclass","Udemy","https://www.udemy.com/course/java-the-complete-java-developer-course"),
     ("Object Oriented Programming in Java","edX","https://www.edx.org/learn/java/object-oriented-programming-in-java"),
     ("Java SE 11 Developer Certification","Pluralsight","https://www.pluralsight.com/paths/java-se-11-developer-certification-1z0-819"),
     ("Java Enterprise Edition","LinkedIn Learning","https://www.linkedin.com/learning/topics/java-enterprise")],
    [("Oracle","Java Developer Intern","Remote","https://www.oracle.com/careers"),
     ("IBM","Software Engineer Intern","Hybrid","https://www.ibm.com/careers"),
     ("SAP","Java Backend Intern","On-site","https://jobs.sap.com")])

write_skill("C++",
    [("C++ For C Programmers","Coursera","https://www.coursera.org/learn/c-plus-plus-a"),
     ("Beginning C++ Programming","Udemy","https://www.udemy.com/course/beginning-c-plus-plus-programming"),
     ("Introduction to C++","edX","https://www.edx.org/learn/c/microsoft-introduction-to-c"),
     ("C++ Fundamentals","Pluralsight","https://www.pluralsight.com/courses/cpp-fundamentals"),
     ("Modern C++ Concurrency","LinkedIn Learning","https://www.linkedin.com/learning/topics/c-plus-plus")],
    [("NVIDIA","C++ Software Intern","Remote","https://www.nvidia.com/en-us/about-nvidia/careers"),
     ("Bloomberg","Software Engineering Intern","On-site","https://www.bloomberg.com/company/careers"),
     ("Adobe","C++ Developer Intern","Hybrid","https://careers.adobe.com")])

write_skill("C",
    [("C Programming: Getting Started","edX","https://www.edx.org/learn/c/dartmouth-c-programming-getting-started"),
     ("C Programming For Beginners","Udemy","https://www.udemy.com/course/c-programming-for-beginners"),
     ("C for Everyone: Programming Fundamentals","Coursera","https://www.coursera.org/learn/c-for-everyone"),
     ("Advanced C Programming","LinkedIn Learning","https://www.linkedin.com/learning/topics/c"),
     ("Embedded C Programming","Udemy","https://www.udemy.com/course/embedded-c-programming")],
    [("Intel","Firmware Engineering Intern","On-site","https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"),
     ("Texas Instruments","Embedded Software Intern","Hybrid","https://careers.ti.com"),
     ("Qualcomm","Embedded Systems Intern","On-site","https://www.qualcomm.com/company/careers")])

write_skill("R",
    [("R Programming","Coursera","https://www.coursera.org/learn/r-programming"),
     ("Data Science with R","DataCamp","https://www.datacamp.com/courses/data-scientist-with-r"),
     ("R for Data Science","Pluralsight","https://www.pluralsight.com/courses/r-data-science"),
     ("Advanced R Programming","LinkedIn Learning","https://www.linkedin.com/learning/topics/r"),
     ("Statistics with R","edX","https://www.edx.org/learn/r/statistics")],
    [("RStudio","Data Science Intern","Remote","https://posit.co/careers"),
     ("Biogen","Biostatistics Intern","Hybrid","https://www.biogen.com/careers"),
     ("Pfizer","R Programming Intern","On-site","https://www.pfizer.com/careers")])

write_skill("JavaScript",
    [("JavaScript: The Advanced Concepts","Udemy","https://www.udemy.com/course/advanced-javascript-concepts"),
     ("JavaScript Algorithms and Data Structures","freeCodeCamp","https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures"),
     ("Modern JavaScript from the Beginning","Udemy","https://www.udemy.com/course/modern-javascript-from-the-beginning"),
     ("JavaScript Essential Training","LinkedIn Learning","https://www.linkedin.com/learning/topics/javascript"),
     ("ES6 JavaScript: The Complete Developer","Pluralsight","https://www.pluralsight.com/courses/javascript-es6")],
    [("Netflix","JavaScript Engineering Intern","Remote","https://jobs.netflix.com"),
     ("Uber","Frontend Engineering Intern","Hybrid","https://www.uber.com/careers"),
     ("Airbnb","Web Platform Intern","On-site","https://careers.airbnb.com")])

write_skill("Node.js",
    [("Node.js, Express, MongoDB Bootcamp","Udemy","https://www.udemy.com/course/nodejs-express-mongodb-bootcamp"),
     ("Server-side Development with NodeJS","Coursera","https://www.coursera.org/learn/server-side-nodejs"),
     ("Node.js Microservices","Pluralsight","https://www.pluralsight.com/courses/node-js-microservices"),
     ("Advanced Node.js","LinkedIn Learning","https://www.linkedin.com/learning/topics/node-js"),
     ("Node.js Design Patterns","Udemy","https://www.udemy.com/course/nodejs-design-patterns")],
    [("PayPal","Node.js Developer Intern","Remote","https://www.paypal.com/us/webapps/mpp/jobs"),
     ("Slack","Backend Engineering Intern","Hybrid","https://slack.com/careers"),
     ("Medium","Platform Engineering Intern","On-site","https://medium.com/jobs")])

write_skill("TypeScript",
    [("Understanding TypeScript","Udemy","https://www.udemy.com/course/understanding-typescript"),
     ("TypeScript Fundamentals","Pluralsight","https://www.pluralsight.com/courses/typescript-fundamentals"),
     ("TypeScript: The Complete Developer","Udemy","https://www.udemy.com/course/typescript-the-complete-developers-guide"),
     ("Advanced TypeScript","LinkedIn Learning","https://www.linkedin.com/learning/topics/typescript"),
     ("TypeScript with React","Coursera","https://www.coursera.org/learn/typescript")],
    [("Linear","TypeScript Engineering Intern","Remote","https://linear.app/careers"),
     ("Notion","Frontend Engineering Intern","Hybrid","https://www.notion.so/careers"),
     ("Figma","Web Engineering Intern","On-site","https://www.figma.com/careers")])

# Fundamentals
write_skill("Data Structures",
    [("Data Structures and Algorithms Specialization","Coursera","https://www.coursera.org/specializations/data-structures-algorithms"),
     ("Master the Coding Interview","Udemy","https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms"),
     ("Data Structures Fundamentals","edX","https://www.edx.org/learn/data-structures"),
     ("Algorithms and Data Structures in Python","Udemy","https://www.udemy.com/course/algorithms-and-data-structures-in-python"),
     ("Data Structures in Java","LinkedIn Learning","https://www.linkedin.com/learning/topics/data-structures")],
    [("Meta","Software Engineering Intern","Remote","https://www.metacareers.com"),
     ("Apple","Algorithms Engineer Intern","On-site","https://jobs.apple.com"),
     ("LinkedIn","Software Engineering Intern","Hybrid","https://careers.linkedin.com")])

write_skill("Algorithms",
    [("Algorithmic Toolbox","Coursera","https://www.coursera.org/learn/algorithmic-toolbox"),
     ("Algorithms Specialization","Coursera","https://www.coursera.org/specializations/algorithms"),
     ("Grokking the Coding Interview","Educative","https://www.educative.io/courses/grokking-the-coding-interview"),
     ("Introduction to Algorithms","MIT OpenCourseWare","https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011"),
     ("Competitive Programming","Codeforces","https://codeforces.com/edu/course/2")],
    [("Two Sigma","Quantitative Research Intern","On-site","https://www.twosigma.com/careers"),
     ("Jane Street","Software Engineering Intern","Hybrid","https://www.janestreet.com/join-jane-street"),
     ("Citadel","Algorithm Engineering Intern","On-site","https://www.citadel.com/careers")])

write_skill("OOP",
    [("Object-Oriented Programming in Java","Coursera","https://www.coursera.org/learn/object-oriented-java"),
     ("OOP in Python","Udemy","https://www.udemy.com/course/object-oriented-programming-python"),
     ("Design Patterns in OOP","Pluralsight","https://www.pluralsight.com/courses/design-patterns-overview"),
     ("SOLID Principles","Coursera","https://www.coursera.org/learn/solid-principles-object-oriented-design"),
     ("OOP Design Patterns","edX","https://www.edx.org/learn/object-oriented-programming")],
    [("Salesforce","Software Engineering Intern","Remote","https://careers.salesforce.com"),
     ("Oracle","Java OOP Developer Intern","Hybrid","https://www.oracle.com/careers"),
     ("Intuit","Software Engineering Intern","On-site","https://www.intuit.com/careers")])

write_skill("Git",
    [("Git and GitHub Specialization","Coursera","https://www.coursera.org/specializations/google-it-automation"),
     ("Git Complete: The Definitive Guide","Udemy","https://www.udemy.com/course/git-complete"),
     ("GitHub Actions","LinkedIn Learning","https://www.linkedin.com/learning/topics/github"),
     ("Advanced Git","Pluralsight","https://www.pluralsight.com/courses/advanced-git"),
     ("Git Fundamentals","Codecademy","https://www.codecademy.com/learn/learn-git")],
    [("GitHub","Software Engineering Intern","Remote","https://github.com/about/careers"),
     ("GitLab","Engineering Intern","Remote","https://about.gitlab.com/jobs"),
     ("Atlassian","DevOps Intern","Hybrid","https://www.atlassian.com/company/careers")])

write_skill("SQL",
    [("SQL for Data Science","Coursera","https://www.coursera.org/learn/sql-for-data-science"),
     ("The Complete SQL Bootcamp","Udemy","https://www.udemy.com/course/the-complete-sql-bootcamp"),
     ("Introduction to SQL","edX","https://www.edx.org/learn/sql"),
     ("Advanced SQL","DataCamp","https://www.datacamp.com/courses/advanced-sql"),
     ("SQL Querying","Khan Academy","https://www.khanacademy.org/computing/computer-programming/sql")],
    [("Snowflake","Data Engineering Intern","Remote","https://careers.snowflake.com"),
     ("Databricks","SQL Analytics Intern","Hybrid","https://www.databricks.com/company/careers"),
     ("MongoDB","Database Engineering Intern","On-site","https://www.mongodb.com/careers")])

write_skill("Linux",
    [("Linux Fundamentals","Pluralsight","https://www.pluralsight.com/courses/linux-fundamentals"),
     ("Linux Administration Bootcamp","Udemy","https://www.udemy.com/course/linux-administration-bootcamp"),
     ("Introduction to Linux","edX","https://www.edx.org/learn/linux"),
     ("Linux Command Line Basics","Codecademy","https://www.codecademy.com/learn/learn-the-command-line"),
     ("Red Hat Certified System Administrator","Coursera","https://www.coursera.org/professional-certificates/red-hat-system-administrator")],
    [("Red Hat","Linux Engineering Intern","Remote","https://www.redhat.com/en/jobs"),
     ("Canonical","Ubuntu Engineering Intern","Remote","https://canonical.com/careers"),
     ("SUSE","Systems Engineering Intern","Hybrid","https://www.suse.com/careers")])

write_skill("REST APIs",
    [("APIs and Microservices","freeCodeCamp","https://www.freecodecamp.org/learn/apis-and-microservices"),
     ("REST API Design","Udemy","https://www.udemy.com/course/rest-api-design"),
     ("Building RESTful APIs with Node.js","Coursera","https://www.coursera.org/learn/server-side-nodejs"),
     ("API Testing with Postman","LinkedIn Learning","https://www.linkedin.com/learning/topics/api"),
     ("GraphQL and REST API Design","Pluralsight","https://www.pluralsight.com/courses/designing-restful-web-apis")],
    [("Stripe","API Engineering Intern","Remote","https://stripe.com/jobs"),
     ("Twilio","Developer Relations Intern","Hybrid","https://www.twilio.com/company/jobs"),
     ("SendGrid","API Developer Intern","On-site","https://sendgrid.com/careers")])

write_skill("RESTful APIs",
    [("REST API Design, Development","Udemy","https://www.udemy.com/course/rest-api-design"),
     ("APIs and Microservices","freeCodeCamp","https://www.freecodecamp.org/learn/apis-and-microservices"),
     ("Web Services and APIs","Coursera","https://www.coursera.org/learn/server-side-nodejs"),
     ("Building REST APIs with Django","LinkedIn Learning","https://www.linkedin.com/learning/topics/api"),
     ("REST API with Spring Boot","Pluralsight","https://www.pluralsight.com/courses/rest-api-spring-boot")],
    [("Stripe","API Engineering Intern","Remote","https://stripe.com/jobs"),
     ("Postman","API Platform Intern","Hybrid","https://www.postman.com/careers"),
     ("RapidAPI","Developer Experience Intern","On-site","https://rapidapi.com/careers")])

write_skill("Testing",
    [("Software Testing and Automation","Coursera","https://www.coursera.org/specializations/software-testing-automation"),
     ("Automation Testing with Selenium","Udemy","https://www.udemy.com/course/selenium-webdriver-with-java"),
     ("Test-Driven Development","Pluralsight","https://www.pluralsight.com/courses/test-driven-development-big-picture"),
     ("Software Testing Fundamentals","edX","https://www.edx.org/learn/software-testing"),
     ("Playwright Test Automation","LinkedIn Learning","https://www.linkedin.com/learning/topics/playwright")],
    [("BrowserStack","QA Engineering Intern","Remote","https://www.browserstack.com/careers"),
     ("Sauce Labs","Test Automation Intern","Hybrid","https://saucelabs.com/company/careers"),
     ("Applitools","Visual AI Testing Intern","On-site","https://applitools.com/careers")])

write_skill("CI/CD",
    [("DevOps, CI/CD","Coursera","https://www.coursera.org/learn/introduction-to-devops"),
     ("Jenkins, From Zero to Hero","Udemy","https://www.udemy.com/course/jenkins-from-zero-to-hero"),
     ("GitHub Actions for CI/CD","LinkedIn Learning","https://www.linkedin.com/learning/topics/github-actions"),
     ("Azure DevOps Fundamentals","Pluralsight","https://www.pluralsight.com/courses/azure-devops-getting-started"),
     ("CI/CD with GitLab","Udemy","https://www.udemy.com/course/gitlab-ci-pipelines")],
    [("CircleCI","Developer Experience Intern","Remote","https://circleci.com/careers"),
     ("GitLab","CI/CD Engineering Intern","Remote","https://about.gitlab.com/jobs"),
     ("Travis CI","DevOps Engineering Intern","Hybrid","https://www.travis-ci.com/careers")])

write_skill("Deployment",
    [("Deploying Applications with Kubernetes","Pluralsight","https://www.pluralsight.com/courses/deploying-applications-kubernetes"),
     ("AWS Deployment Fundamentals","Udemy","https://www.udemy.com/course/aws-deployment"),
     ("Heroku Deployment Mastery","LinkedIn Learning","https://www.linkedin.com/learning/topics/heroku"),
     ("Docker Deployment","Coursera","https://www.coursera.org/learn/deploying-apps-with-docker"),
     ("Vercel and Netlify Deployment","Udemy","https://www.udemy.com/course/deployment-vercel-netlify")],
    [("Vercel","Platform Engineering Intern","Remote","https://vercel.com/careers"),
     ("Heroku","Infrastructure Intern","Hybrid","https://www.heroku.com/careers"),
     ("DigitalOcean","Cloud Engineering Intern","On-site","https://www.digitalocean.com/careers")])

write_skill("Caching",
    [("Redis Caching Fundamentals","Udemy","https://www.udemy.com/course/redis-caching"),
     ("System Design: Caching Strategies","Educative","https://www.educative.io/courses/grokking-system-design"),
     ("Memcached and Redis","Pluralsight","https://www.pluralsight.com/courses/redis-fundamentals"),
     ("CDN and Edge Caching","LinkedIn Learning","https://www.linkedin.com/learning/topics/caching"),
     ("High Performance Caching","Coursera","https://www.coursera.org/learn/scalable-software-architecture")],
    [("Redis","Software Engineering Intern","Remote","https://redis.com/careers"),
     ("Cloudflare","Edge Computing Intern","Hybrid","https://www.cloudflare.com/careers"),
     ("Fastly","Caching Infrastructure Intern","On-site","https://www.fastly.com/careers")])

write_skill("Authentication",
    [("OAuth 2.0 and OpenID Connect","Udemy","https://www.udemy.com/course/oauth-2-and-openid-connect"),
     ("Authentication and Authorization","Pluralsight","https://www.pluralsight.com/courses/authentication-authorization-asp-dot-net-core"),
     ("JSON Web Tokens (JWT)","LinkedIn Learning","https://www.linkedin.com/learning/topics/authentication"),
     ("Identity and Access Management","Coursera","https://www.coursera.org/learn/identity-and-access-management"),
     ("SSO and SAML","Udemy","https://www.udemy.com/course/saml-sso")],
    [("Okta","Identity Engineering Intern","Remote","https://www.okta.com/company/careers"),
     ("Auth0","Security Engineering Intern","Hybrid","https://auth0.com/careers"),
     ("Ping Identity","IAM Engineering Intern","On-site","https://www.pingidentity.com/en/company/careers")])

write_skill("Databases",
    [("Database Systems Concepts","Coursera","https://www.coursera.org/learn/database-systems"),
     ("MongoDB Complete Guide","Udemy","https://www.udemy.com/course/mongodb-the-complete-developers-guide"),
     ("PostgreSQL Advanced","Pluralsight","https://www.pluralsight.com/courses/postgresql-fundamentals"),
     ("Database Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/database-management"),
     ("NoSQL Database Essentials","edX","https://www.edx.org/learn/nosql-databases")],
    [("MongoDB","Database Engineering Intern","Remote","https://www.mongodb.com/careers"),
     ("Cockroach Labs","Distributed Systems Intern","Hybrid","https://www.cockroachlabs.com/careers"),
     ("Neo4j","Graph Database Intern","On-site","https://neo4j.com/careers")])

write_skill("Microservices",
    [("Microservices with Spring Boot","Udemy","https://www.udemy.com/course/microservices-with-spring-boot-and-spring-cloud"),
     ("Building Microservices","Pluralsight","https://www.pluralsight.com/courses/building-microservices"),
     ("Microservices Architecture","Coursera","https://www.coursera.org/learn/microservices"),
     ("AWS Microservices","LinkedIn Learning","https://www.linkedin.com/learning/topics/microservices"),
     ("Microservices Patterns","edX","https://www.edx.org/learn/microservices")],
    [("Netflix","Microservices Engineering Intern","Remote","https://jobs.netflix.com"),
     ("Uber","Platform Engineering Intern","Hybrid","https://www.uber.com/careers"),
     ("Lyft","Distributed Systems Intern","On-site","https://www.lyft.com/careers")])

# Web Development
write_skill("HTML",
    [("HTML and CSS Fundamentals","Codecademy","https://www.codecademy.com/learn/learn-html"),
     ("HTML5 from Scratch","Udemy","https://www.udemy.com/course/html5-from-scratch"),
     ("Web Design for Everybody","Coursera","https://www.coursera.org/specializations/web-design"),
     ("HTML Essential Training","LinkedIn Learning","https://www.linkedin.com/learning/topics/html"),
     ("Responsive Web Design","freeCodeCamp","https://www.freecodecamp.org/learn/2022/responsive-web-design")],
    [("Vercel","Frontend Engineering Intern","Remote","https://vercel.com/careers"),
     ("Shopify","Web Developer Intern","Hybrid","https://www.shopify.com/careers"),
     ("Wix","Web Platform Intern","On-site","https://www.wix.com/jobs")])

write_skill("CSS",
    [("Advanced CSS and Sass","Udemy","https://www.udemy.com/course/advanced-css-and-sass"),
     ("CSS Grid and Flexbox","LinkedIn Learning","https://www.linkedin.com/learning/topics/css"),
     ("Modern CSS","Pluralsight","https://www.pluralsight.com/courses/modern-css"),
     ("CSS Animation Masterclass","Udemy","https://www.udemy.com/course/css-animation"),
     ("Tailwind CSS Fundamentals","Codecademy","https://www.codecademy.com/learn/learn-tailwind-css")],
    [("Figma","Design Engineering Intern","Remote","https://www.figma.com/careers"),
     ("Canva","Frontend Engineering Intern","Hybrid","https://www.canva.com/careers"),
     ("Webflow","Web Design Intern","On-site","https://webflow.com/careers")])

write_skill("React",
    [("React - The Complete Guide","Udemy","https://www.udemy.com/course/react-the-complete-guide-incl-redux"),
     ("Front-End Web Development with React","Coursera","https://www.coursera.org/learn/front-end-react"),
     ("React.js Essential Training","LinkedIn Learning","https://www.linkedin.com/learning/topics/react-js"),
     ("Advanced React Patterns","Pluralsight","https://www.pluralsight.com/courses/reactjs-advanced"),
     ("React Native: Advanced Concepts","Udemy","https://www.udemy.com/course/react-native-advanced")],
    [("Meta","React Engineering Intern","Remote","https://www.metacareers.com"),
     ("Vercel","Next.js Engineering Intern","Hybrid","https://vercel.com/careers"),
     ("Discord","Frontend Engineering Intern","On-site","https://discord.com/careers")])

write_skill("Next.js",
    [("Next.js 14 Complete Developer Guide","Udemy","https://www.udemy.com/course/nextjs-react-the-complete-guide"),
     ("Full-Stack Development with Next.js","Coursera","https://www.coursera.org/learn/nextjs"),
     ("Next.js Production Patterns","Pluralsight","https://www.pluralsight.com/courses/nextjs-fundamentals"),
     ("Advanced Next.js","LinkedIn Learning","https://www.linkedin.com/learning/topics/next-js"),
     ("Server Components with Next.js","Udemy","https://www.udemy.com/course/nextjs-server-components")],
    [("Vercel","Framework Engineering Intern","Remote","https://vercel.com/careers"),
     ("Notion","Full Stack Engineering Intern","Hybrid","https://www.notion.so/careers"),
     ("HashiCorp","Developer Tools Intern","On-site","https://www.hashicorp.com/careers")])

write_skill("Responsive Design",
    [("Responsive Web Design","freeCodeCamp","https://www.freecodecamp.org/learn/2022/responsive-web-design"),
     ("Mobile-First Responsive Design","Udemy","https://www.udemy.com/course/mobile-first-responsive-design"),
     ("Responsive Design with CSS","LinkedIn Learning","https://www.linkedin.com/learning/topics/responsive-design"),
     ("Bootstrap 5 From Scratch","Pluralsight","https://www.pluralsight.com/courses/bootstrap-5-fundamentals"),
     ("Material UI Design","Coursera","https://www.coursera.org/learn/material-design")],
    [("Apple","UI Engineering Intern","Remote","https://jobs.apple.com"),
     ("Spotify","Design Engineering Intern","Hybrid","https://www.lifeatspotify.com/jobs"),
     ("Pinterest","Web Platform Intern","On-site","https://www.pinterestcareers.com")])

write_skill("Accessibility",
    [("Web Accessibility","Coursera","https://www.coursera.org/learn/web-accessibility"),
     ("Accessibility for Web Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/accessibility"),
     ("A11y Testing","Udemy","https://www.udemy.com/course/web-accessibility-testing"),
     ("WCAG 2.1 Compliance","Pluralsight","https://www.pluralsight.com/courses/web-accessibility-wcag"),
     ("Inclusive Design","edX","https://www.edx.org/learn/accessibility")],
    [("Deque Systems","A11y Engineering Intern","Remote","https://www.deque.com/company/careers"),
     ("Microsoft","Inclusive Design Intern","Hybrid","https://careers.microsoft.com"),
     ("Apple","Accessibility Engineering Intern","On-site","https://jobs.apple.com")])

write_skill("Performance Optimization",
    [("Web Performance Fundamentals","Udemy","https://www.udemy.com/course/web-performance"),
     ("High Performance Browser Networking","Pluralsight","https://www.pluralsight.com/courses/web-performance"),
     ("Core Web Vitals","LinkedIn Learning","https://www.linkedin.com/learning/topics/web-performance"),
     ("Frontend Performance","Coursera","https://www.coursera.org/learn/frontend-performance"),
     ("Lighthouse and PageSpeed","Udemy","https://www.udemy.com/course/lighthouse-pagespeed")],
    [("Google","Chrome Performance Intern","Remote","https://careers.google.com"),
     ("Cloudflare","Edge Performance Intern","Hybrid","https://www.cloudflare.com/careers"),
     ("Akamai","CDN Performance Intern","On-site","https://www.akamai.com/company/careers")])

write_skill("State Management",
    [("Redux Toolkit Complete Guide","Udemy","https://www.udemy.com/course/redux-toolkit-complete-guide"),
     ("Zustand and React State","Pluralsight","https://www.pluralsight.com/courses/react-state-management"),
     ("Context API and Hooks","LinkedIn Learning","https://www.linkedin.com/learning/topics/react-state-management"),
     ("MobX State Management","Udemy","https://www.udemy.com/course/mobx-state-management"),
     ("Recoil for React","Coursera","https://www.coursera.org/learn/react-state-management")],
    [("Meta","React State Intern","Remote","https://www.metacareers.com"),
     ("Vercel","Frontend Engineering Intern","Hybrid","https://vercel.com/careers"),
     ("Redux","Open Source Intern","On-site","https://redux.js.org")])

write_skill("SEO",
    [("SEO Specialization","Coursera","https://www.coursera.org/specializations/seo"),
     ("Technical SEO","Udemy","https://www.udemy.com/course/technical-seo"),
     ("SEO Fundamentals","LinkedIn Learning","https://www.linkedin.com/learning/topics/seo"),
     ("Advanced SEO Strategies","Pluralsight","https://www.pluralsight.com/courses/seo-fundamentals"),
     ("Content SEO Mastery","Udemy","https://www.udemy.com/course/content-seo")],
    [("HubSpot","SEO Engineering Intern","Remote","https://www.hubspot.com/careers"),
     ("Semrush","SEO Tools Intern","Hybrid","https://www.semrush.com/company/careers"),
     ("Ahrefs","Technical SEO Intern","On-site","https://ahrefs.com/careers")])

# Data Science
write_skill("Machine Learning",
    [("Machine Learning Specialization","Coursera","https://www.coursera.org/specializations/machine-learning-introduction"),
     ("Machine Learning A-Z","Udemy","https://www.udemy.com/course/machinelearning"),
     ("Applied Machine Learning","edX","https://www.edx.org/learn/machine-learning"),
     ("Hands-On Machine Learning","Pluralsight","https://www.pluralsight.com/courses/machine-learning-fundamentals"),
     ("Machine Learning with Python","DataCamp","https://www.datacamp.com/courses/machine-learning-with-python")],
    [("Google","Machine Learning Intern","Remote","https://careers.google.com"),
     ("Apple","ML Platform Intern","Hybrid","https://jobs.apple.com"),
     ("OpenAI","Research Intern","On-site","https://openai.com/careers")])

write_skill("Deep Learning",
    [("Deep Learning Specialization","Coursera","https://www.coursera.org/specializations/deep-learning"),
     ("Deep Learning A-Z","Udemy","https://www.udemy.com/course/deeplearning"),
     ("Neural Networks and Deep Learning","Coursera","https://www.coursera.org/learn/neural-networks-deep-learning"),
     ("Practical Deep Learning","fast.ai","https://www.fast.ai"),
     ("PyTorch Deep Learning","Pluralsight","https://www.pluralsight.com/courses/pytorch-fundamentals")],
    [("DeepMind","Research Intern","Remote","https://deepmind.com/careers"),
     ("NVIDIA","Deep Learning Intern","Hybrid","https://www.nvidia.com/en-us/about-nvidia/careers"),
     ("Stability AI","Generative AI Intern","On-site","https://stability.ai/careers")])

write_skill("TensorFlow",
    [("TensorFlow Developer Certificate","Coursera","https://www.coursera.org/professional-certificates/tensorflow-in-practice"),
     ("TensorFlow 2.0 Complete Guide","Udemy","https://www.udemy.com/course/tensorflow-developer-certificate-machine-learning-zero-to-mastery"),
     ("TensorFlow.js","Pluralsight","https://www.pluralsight.com/courses/tensorflow-js-getting-started"),
     ("Advanced TensorFlow","LinkedIn Learning","https://www.linkedin.com/learning/topics/tensorflow"),
     ("TensorFlow for Deep Learning","DataCamp","https://www.datacamp.com/courses/deep-learning-with-tensorflow")],
    [("Google","TensorFlow Engineering Intern","Remote","https://careers.google.com"),
     ("NVIDIA","ML Frameworks Intern","Hybrid","https://www.nvidia.com/en-us/about-nvidia/careers"),
     ("Hugging Face","ML Engineering Intern","On-site","https://huggingface.co/careers")])

write_skill("PyTorch",
    [("PyTorch for Deep Learning","Udemy","https://www.udemy.com/course/pytorch-for-deep-learning"),
     ("Deep Learning with PyTorch","Coursera","https://www.coursera.org/learn/deep-neural-networks-with-pytorch"),
     ("PyTorch Fundamentals","Pluralsight","https://www.pluralsight.com/courses/pytorch-fundamentals"),
     ("Practical PyTorch","LinkedIn Learning","https://www.linkedin.com/learning/topics/pytorch"),
     ("PyTorch for Computer Vision","DataCamp","https://www.datacamp.com/courses/introduction-to-deep-learning-with-pytorch")],
    [("Meta AI","PyTorch Engineering Intern","Remote","https://www.metacareers.com"),
     ("NVIDIA","Deep Learning Frameworks Intern","Hybrid","https://www.nvidia.com/en-us/about-nvidia/careers"),
     ("OpenAI","Research Engineering Intern","On-site","https://openai.com/careers")])

write_skill("Pandas",
    [("Data Analysis with Pandas","Udemy","https://www.udemy.com/course/data-analysis-with-pandas"),
     ("Pandas Fundamentals","Pluralsight","https://www.pluralsight.com/courses/pandas-fundamentals"),
     ("Data Manipulation with Pandas","DataCamp","https://www.datacamp.com/courses/data-manipulation-with-pandas"),
     ("Pandas for Data Science","Coursera","https://www.coursera.org/learn/data-analysis-with-python"),
     ("Advanced Pandas Techniques","LinkedIn Learning","https://www.linkedin.com/learning/topics/pandas")],
    [("Kaggle","Data Science Intern","Remote","https://www.kaggle.com/careers"),
     ("DataRobot","ML Engineering Intern","Hybrid","https://www.datarobot.com/careers"),
     ("Palantir","Data Engineering Intern","On-site","https://www.palantir.com/careers")])

write_skill("NumPy",
    [("NumPy for Data Science","Udemy","https://www.udemy.com/course/numpy-for-data-science"),
     ("NumPy Fundamentals","Pluralsight","https://www.pluralsight.com/courses/numpy-fundamentals"),
     ("Scientific Computing with Python","freeCodeCamp","https://www.freecodecamp.org/learn/scientific-computing-with-python"),
     ("NumPy and SciPy","DataCamp","https://www.datacamp.com/courses/introduction-to-numpy"),
     ("Advanced NumPy","LinkedIn Learning","https://www.linkedin.com/learning/topics/numpy")],
    [("Anaconda","Scientific Computing Intern","Remote","https://www.anaconda.com/careers"),
     ("Quansight","Open Source Intern","Hybrid","https://quansight.com/careers"),
     ("NumFOCUS","Data Science Intern","On-site","https://numfocus.org")])
