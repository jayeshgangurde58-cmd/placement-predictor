#!/usr/bin/env python3
"""Append remaining skills to course_database.py."""

def append_skill(name, courses, internships):
    with open('backend/services/course_database.py', 'a', encoding='utf-8') as f:
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

# Data Science
append_skill("Matplotlib",
    [("Matplotlib for Data Visualization","Udemy","https://www.udemy.com/course/matplotlib-for-data-visualization"),
     ("Data Visualization with Python","Coursera","https://www.coursera.org/learn/python-for-data-visualization"),
     ("Matplotlib Fundamentals","Pluralsight","https://www.pluralsight.com/courses/matplotlib-fundamentals"),
     ("Python Data Visualization","LinkedIn Learning","https://www.linkedin.com/learning/topics/data-visualization"),
     ("Advanced Matplotlib","DataCamp","https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib")],
    [("Tableau","Data Visualization Intern","Remote","https://www.tableau.com/careers"),
     ("Plotly","Frontend Engineering Intern","Hybrid","https://plotly.com/careers"),
     ("Observable","Visualization Engineering Intern","On-site","https://observablehq.com/careers")])

append_skill("Statistics",
    [("Statistics with Python","Coursera","https://www.coursera.org/specializations/statistics-with-python"),
     ("Practical Statistics","Udemy","https://www.udemy.com/course/statistics-for-data-science"),
     ("Introduction to Statistics","edX","https://www.edx.org/learn/statistics"),
     ("Statistics Fundamentals","Pluralsight","https://www.pluralsight.com/courses/statistics-fundamentals"),
     ("Bayesian Statistics","DataCamp","https://www.datacamp.com/courses/introduction-to-statistics")],
    [("Capital One","Data Science Intern","Remote","https://www.capitalone.com/careers"),
     ("JPMorgan Chase","Quantitative Research Intern","Hybrid","https://www.jpmorganchase.com/careers"),
     ("Goldman Sachs","Quantitative Analyst Intern","On-site","https://www.goldmansachs.com/careers")])

append_skill("Data Visualization",
    [("Data Visualization with Tableau","Coursera","https://www.coursera.org/specializations/data-visualization"),
     ("Data Visualization with Python","Udemy","https://www.udemy.com/course/data-visualization-with-python"),
     ("Information Visualization","edX","https://www.edx.org/learn/data-visualization"),
     ("D3.js Data Visualization","Pluralsight","https://www.pluralsight.com/courses/d3js-data-visualization-fundamentals"),
     ("Power BI Data Visualization","LinkedIn Learning","https://www.linkedin.com/learning/topics/power-bi")],
    [("Tableau","Data Visualization Intern","Remote","https://www.tableau.com/careers"),
     ("Looker","Analytics Engineering Intern","Hybrid","https://www.looker.com/careers"),
     ("Mode Analytics","Data Science Intern","On-site","https://mode.com/careers")])

append_skill("Data Preprocessing",
    [("Data Preprocessing with Python","Udemy","https://www.udemy.com/course/data-preprocessing"),
     ("Feature Engineering","Coursera","https://www.coursera.org/learn/feature-engineering"),
     ("Data Cleaning Fundamentals","DataCamp","https://www.datacamp.com/courses/cleaning-data-in-python"),
     ("ETL and Data Pipelines","Pluralsight","https://www.pluralsight.com/courses/etl-data-warehousing"),
     ("Data Wrangling","LinkedIn Learning","https://www.linkedin.com/learning/topics/data-wrangling")],
    [("Databricks","Data Engineering Intern","Remote","https://www.databricks.com/company/careers"),
     ("Fivetran","Data Integration Intern","Hybrid","https://www.fivetran.com/careers"),
     ("Stitch Data","ETL Engineering Intern","On-site","https://www.stitchdata.com/careers")])

append_skill("Model Deployment",
    [("ML Model Deployment","Udemy","https://www.udemy.com/course/machine-learning-model-deployment"),
     ("MLOps Specialization","Coursera","https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"),
     ("Deploying ML Models","Pluralsight","https://www.pluralsight.com/courses/deploying-machine-learning-models"),
     ("Kubernetes for ML","LinkedIn Learning","https://www.linkedin.com/learning/topics/mlops"),
     ("AWS SageMaker Deployment","DataCamp","https://www.datacamp.com/courses/introduction-to-aws-sagemaker")],
    [("Seldon","ML Engineering Intern","Remote","https://www.seldon.io/careers"),
     ("Algorithmia","ML Platform Intern","Hybrid","https://algorithmia.com/careers"),
     ("Weights & Biases","MLOps Engineering Intern","On-site","https://wandb.ai/careers")])

append_skill("NLP",
    [("NLP Specialization","Coursera","https://www.coursera.org/specializations/natural-language-processing"),
     ("NLP with Python","Udemy","https://www.udemy.com/course/nlp-natural-language-processing-with-python"),
     ("Transformers for NLP","Pluralsight","https://www.pluralsight.com/courses/transformers-natural-language-processing"),
     ("spaCy for NLP","LinkedIn Learning","https://www.linkedin.com/learning/topics/natural-language-processing"),
     ("Hugging Face NLP","DataCamp","https://www.datacamp.com/courses/introduction-to-nlp")],
    [("Hugging Face","NLP Engineering Intern","Remote","https://huggingface.co/careers"),
     ("AI2","Research Intern","Hybrid","https://allenai.org/careers"),
     ("Grammarly","NLP Engineering Intern","On-site","https://www.grammarly.com/jobs")])

append_skill("Computer Vision",
    [("Computer Vision Basics","Coursera","https://www.coursera.org/learn/computer-vision-basics"),
     ("Deep Learning for Computer Vision","Udemy","https://www.udemy.com/course/deep-learning-computer-vision"),
     ("OpenCV for Computer Vision","Pluralsight","https://www.pluralsight.com/courses/opencv-fundamentals"),
     ("Advanced Computer Vision","LinkedIn Learning","https://www.linkedin.com/learning/topics/computer-vision"),
     ("YOLO and Object Detection","DataCamp","https://www.datacamp.com/courses/object-detection")],
    [("Tesla","Computer Vision Intern","Remote","https://www.tesla.com/careers"),
     ("Waymo","Perception Engineering Intern","Hybrid","https://waymo.com/careers"),
     ("Argo AI","CV Engineering Intern","On-site","https://www.argo.ai/careers")])

# DevOps & Cloud
append_skill("Docker",
    [("Docker and Kubernetes","Udemy","https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide"),
     ("Docker Fundamentals","Pluralsight","https://www.pluralsight.com/courses/docker-fundamentals"),
     ("Containerization with Docker","Coursera","https://www.coursera.org/learn/containerization-docker"),
     ("Docker for Developers","LinkedIn Learning","https://www.linkedin.com/learning/topics/docker"),
     ("Advanced Docker","DataCamp","https://www.datacamp.com/courses/docker-for-data-science")],
    [("Docker Inc","Software Engineering Intern","Remote","https://www.docker.com/careers"),
     ("Mirantis","Container Engineering Intern","Hybrid","https://www.mirantis.com/careers"),
     ("Portworx","Storage Engineering Intern","On-site","https://portworx.com/careers")])

append_skill("Kubernetes",
    [("Kubernetes for Beginners","Udemy","https://www.udemy.com/course/learn-kubernetes"),
     ("Certified Kubernetes Administrator","Pluralsight","https://www.pluralsight.com/paths/certified-kubernetes-administrator"),
     ("Kubernetes Fundamentals","Coursera","https://www.coursera.org/learn/google-kubernetes-engine"),
     ("Advanced Kubernetes","LinkedIn Learning","https://www.linkedin.com/learning/topics/kubernetes"),
     ("Kubernetes in Production","DataCamp","https://www.datacamp.com/courses/kubernetes-fundamentals")],
    [("Google","Kubernetes Engineering Intern","Remote","https://careers.google.com"),
     ("Rancher Labs","Platform Engineering Intern","Hybrid","https://www.rancher.com/careers"),
     ("Red Hat","OpenShift Engineering Intern","On-site","https://www.redhat.com/en/jobs")])

append_skill("AWS",
    [("AWS Solutions Architect","Udemy","https://www.udemy.com/course/aws-certified-solutions-architect-associate"),
     ("AWS Fundamentals","Coursera","https://www.coursera.org/specializations/aws-fundamentals"),
     ("AWS Developer Certification","Pluralsight","https://www.pluralsight.com/paths/aws-certified-developer-associate"),
     ("Serverless on AWS","LinkedIn Learning","https://www.linkedin.com/learning/topics/amazon-web-services"),
     ("AWS Machine Learning","DataCamp","https://www.datacamp.com/courses/introduction-to-aws")],
    [("Amazon Web Services","Cloud Engineering Intern","Remote","https://www.amazon.jobs"),
     ("Cloudflare","Edge Platform Intern","Hybrid","https://www.cloudflare.com/careers"),
     ("Datadog","Cloud Monitoring Intern","On-site","https://www.datadoghq.com/careers")])

append_skill("Azure",
    [("Azure Fundamentals","Udemy","https://www.udemy.com/course/azure-fundamentals"),
     ("Microsoft Azure Certification","Coursera","https://www.coursera.org/professional-certificates/microsoft-azure-fundamentals"),
     ("Azure Developer","Pluralsight","https://www.pluralsight.com/paths/azure-developer-certification"),
     ("Azure DevOps","LinkedIn Learning","https://www.linkedin.com/learning/topics/microsoft-azure"),
     ("Azure Machine Learning","DataCamp","https://www.datacamp.com/courses/introduction-to-azure-ml")],
    [("Microsoft","Azure Engineering Intern","Remote","https://careers.microsoft.com"),
     ("HashiCorp","Cloud Engineering Intern","Hybrid","https://www.hashicorp.com/careers"),
     ("Pulumi","Infrastructure Engineering Intern","On-site","https://www.pulumi.com/careers")])

append_skill("Google Cloud",
    [("Google Cloud Fundamentals","Coursera","https://www.coursera.org/learn/gcp-fundamentals"),
     ("GCP Professional Certification","Udemy","https://www.udemy.com/course/google-cloud-professional-cloud-architect"),
     ("Google Cloud Essentials","Pluralsight","https://www.pluralsight.com/courses/google-cloud-platform-essentials"),
     ("GCP Data Engineering","LinkedIn Learning","https://www.linkedin.com/learning/topics/google-cloud-platform"),
     ("Serverless GCP","DataCamp","https://www.datacamp.com/courses/introduction-to-gcp")],
    [("Google","Cloud Engineering Intern","Remote","https://careers.google.com"),
     ("Elastic","Search Engineering Intern","Hybrid","https://www.elastic.co/careers"),
     ("MongoDB Atlas","Cloud Engineering Intern","On-site","https://www.mongodb.com/careers")])

append_skill("Terraform",
    [("Terraform for AWS","Udemy","https://www.udemy.com/course/terraform-aws"),
     ("Infrastructure as Code with Terraform","Pluralsight","https://www.pluralsight.com/courses/terraform-getting-started"),
     ("Terraform Fundamentals","Coursera","https://www.coursera.org/learn/terraform-for-aws"),
     ("Advanced Terraform","LinkedIn Learning","https://www.linkedin.com/learning/topics/terraform"),
     ("Terraform and Vault","DataCamp","https://www.datacamp.com/courses/terraform-fundamentals")],
    [("HashiCorp","Terraform Engineering Intern","Remote","https://www.hashicorp.com/careers"),
     ("Spacelift","Infrastructure Intern","Hybrid","https://spacelift.io/careers"),
     ("Env0","DevOps Engineering Intern","On-site","https://www.env0.com/careers")])

append_skill("Jenkins",
    [("Jenkins for DevOps","Udemy","https://www.udemy.com/course/jenkins-from-zero-to-hero"),
     ("Jenkins Pipeline Fundamentals","Pluralsight","https://www.pluralsight.com/courses/jenkins-fundamentals"),
     ("Jenkins Administration","Coursera","https://www.coursera.org/learn/jenkins-administration"),
     ("Advanced Jenkins","LinkedIn Learning","https://www.linkedin.com/learning/topics/jenkins"),
     ("Jenkins and Docker","DataCamp","https://www.datacamp.com/courses/jenkins-fundamentals")],
    [("CloudBees","Jenkins Engineering Intern","Remote","https://www.cloudbees.com/careers"),
     ("JFrog","DevOps Engineering Intern","Hybrid","https://jfrog.com/careers"),
     ("Sonatype","Security Engineering Intern","On-site","https://www.sonatype.com/careers")])

append_skill("Ansible",
    [("Ansible for DevOps","Udemy","https://www.udemy.com/course/ansible-for-devops"),
     ("Ansible Fundamentals","Pluralsight","https://www.pluralsight.com/courses/ansible-fundamentals"),
     ("Red Hat Ansible","Coursera","https://www.coursera.org/learn/ansible-red-hat"),
     ("Advanced Ansible","LinkedIn Learning","https://www.linkedin.com/learning/topics/ansible"),
     ("Ansible Automation","DataCamp","https://www.datacamp.com/courses/ansible-fundamentals")],
    [("Red Hat","Automation Engineering Intern","Remote","https://www.redhat.com/en/jobs"),
     ("Ansible","Software Engineering Intern","Hybrid","https://www.ansible.com/careers"),
     ("Puppet","Infrastructure Engineering Intern","On-site","https://puppet.com/careers")])

append_skill("Monitoring",
    [("Monitoring and Observability","Udemy","https://www.udemy.com/course/monitoring-and-observability"),
     ("Prometheus and Grafana","Pluralsight","https://www.pluralsight.com/courses/prometheus-grafana-getting-started"),
     ("Datadog Monitoring","Coursera","https://www.coursera.org/learn/monitoring-cloud"),
     ("New Relic Observability","LinkedIn Learning","https://www.linkedin.com/learning/topics/observability"),
     ("ELK Stack Monitoring","DataCamp","https://www.datacamp.com/courses/elasticsearch-fundamentals")],
    [("Datadog","Observability Engineering Intern","Remote","https://www.datadoghq.com/careers"),
     ("New Relic","Software Engineering Intern","Hybrid","https://newrelic.com/careers"),
     ("Dynatrace","AI Engineering Intern","On-site","https://www.dynatrace.com/careers")])

append_skill("Infrastructure as Code",
    [("Infrastructure as Code","Udemy","https://www.udemy.com/course/infrastructure-as-code"),
     ("IaC with Terraform","Pluralsight","https://www.pluralsight.com/courses/terraform-getting-started"),
     ("CloudFormation and IaC","Coursera","https://www.coursera.org/learn/aws-cloudformation"),
     ("Pulumi Fundamentals","LinkedIn Learning","https://www.linkedin.com/learning/topics/infrastructure-as-code"),
     ("AWS CDK","DataCamp","https://www.datacamp.com/courses/aws-cdk-fundamentals")],
    [("HashiCorp","IaC Engineering Intern","Remote","https://www.hashicorp.com/careers"),
     ("Pulumi","Platform Engineering Intern","Hybrid","https://www.pulumi.com/careers"),
     ("AWS","Cloud Engineering Intern","On-site","https://www.amazon.jobs")])

# Security
append_skill("Network Security",
    [("Network Security Fundamentals","Coursera","https://www.coursera.org/learn/network-security"),
     ("CompTIA Security+","Udemy","https://www.udemy.com/course/comptia-security-certification-sy0-601"),
     ("Network Security Essentials","Pluralsight","https://www.pluralsight.com/courses/network-security-fundamentals"),
     ("Cisco CCNA Security","LinkedIn Learning","https://www.linkedin.com/learning/topics/network-security"),
     ("Advanced Network Security","DataCamp","https://www.datacamp.com/courses/network-security")],
    [("Cisco","Security Engineering Intern","Remote","https://jobs.cisco.com"),
     ("Palo Alto Networks","Network Security Intern","Hybrid","https://www.paloaltonetworks.com/company/careers"),
     ("Fortinet","Cybersecurity Intern","On-site","https://www.fortinet.com/corporate/careers")])

append_skill("Firewalls",
    [("Firewall Fundamentals","Udemy","https://www.udemy.com/course/firewall-fundamentals"),
     ("Palo Alto Firewall","Pluralsight","https://www.pluralsight.com/courses/palo-alto-firewall-fundamentals"),
     ("Firewall Configuration","Coursera","https://www.coursera.org/learn/network-security"),
     ("Advanced Firewall","LinkedIn Learning","https://www.linkedin.com/learning/topics/firewalls"),
     ("pfSense and OPNsense","DataCamp","https://www.datacamp.com/courses/network-security")],
    [("Palo Alto Networks","Firewall Engineering Intern","Remote","https://www.paloaltonetworks.com/company/careers"),
     ("Fortinet","Security Engineering Intern","Hybrid","https://www.fortinet.com/corporate/careers"),
     ("Check Point","Network Security Intern","On-site","https://www.checkpoint.com/careers")])

append_skill("Encryption",
    [("Cryptography Fundamentals","Coursera","https://www.coursera.org/learn/crypto"),
     ("Applied Cryptography","Udemy","https://www.udemy.com/course/applied-cryptography"),
     ("Encryption and Hashing","Pluralsight","https://www.pluralsight.com/courses/cryptography-fundamentals"),
     ("Public Key Infrastructure","LinkedIn Learning","https://www.linkedin.com/learning/topics/cryptography"),
     ("Quantum Cryptography","DataCamp","https://www.datacamp.com/courses/cryptography-fundamentals")],
    [("Cloudflare","Cryptography Engineering Intern","Remote","https://www.cloudflare.com/careers"),
     ("Keybase","Security Engineering Intern","Hybrid","https://keybase.io"),
     ("Let's Encrypt","Security Engineering Intern","On-site","https://letsencrypt.org")])

append_skill("SIEM",
    [("SIEM Fundamentals","Udemy","https://www.udemy.com/course/siem-fundamentals"),
     ("Splunk Fundamentals","Pluralsight","https://www.pluralsight.com/courses/splunk-fundamentals"),
     ("ELK Stack for SIEM","Coursera","https://www.coursera.org/learn/elastic-stack"),
     ("QRadar SIEM","LinkedIn Learning","https://www.linkedin.com/learning/topics/siem"),
     ("Splunk Administration","DataCamp","https://www.datacamp.com/courses/splunk-fundamentals")],
    [("Splunk","SIEM Engineering Intern","Remote","https://www.splunk.com/careers"),
     ("Elastic","Security Engineering Intern","Hybrid","https://www.elastic.co/careers"),
     ("IBM Security","Cybersecurity Intern","On-site","https://www.ibm.com/careers")])

append_skill("Vulnerability Assessment",
    [("Vulnerability Assessment","Udemy","https://www.udemy.com/course/vulnerability-assessment"),
     ("Ethical Hacking","Pluralsight","https://www.pluralsight.com/courses/ethical-hacking-understanding"),
     ("Penetration Testing","Coursera","https://www.coursera.org/learn/penetration-testing"),
     ("OWASP Top 10","LinkedIn Learning","https://www.linkedin.com/learning/topics/penetration-testing"),
     ("Burp Suite","DataCamp","https://www.datacamp.com/courses/penetration-testing")],
    [("Rapid7","Security Engineering Intern","Remote","https://www.rapid7.com/careers"),
     ("Tenable","Vulnerability Research Intern","Hybrid","https://www.tenable.com/careers"),
     ("Qualys","Security Engineering Intern","On-site","https://www.qualys.com/careers")])

append_skill("Incident Response",
    [("Incident Response","Udemy","https://www.udemy.com/course/incident-response"),
     ("DFIR Fundamentals","Pluralsight","https://www.pluralsight.com/courses/digital-forensics-incident-response"),
     ("Cybersecurity Incident Response","Coursera","https://www.coursera.org/learn/cybersecurity-incident-response"),
     ("SOC Operations","LinkedIn Learning","https://www.linkedin.com/learning/topics/incident-response"),
     ("Threat Hunting","DataCamp","https://www.datacamp.com/courses/cybersecurity-fundamentals")],
    [("Mandiant","Incident Response Intern","Remote","https://www.mandiant.com/careers"),
     ("CrowdStrike","Security Engineering Intern","Hybrid","https://www.crowdstrike.com/careers"),
     ("FireEye","Threat Intelligence Intern","On-site","https://www.fireeye.com/careers")])

append_skill("Risk Management",
    [("Risk Management Fundamentals","Udemy","https://www.udemy.com/course/risk-management-fundamentals"),
     ("Cyber Risk Management","Pluralsight","https://www.pluralsight.com/courses/cyber-risk-management"),
     ("Enterprise Risk","Coursera","https://www.coursera.org/learn/operational-risk-management"),
     ("GRC Fundamentals","LinkedIn Learning","https://www.linkedin.com/learning/topics/risk-management"),
     ("ISO 27001","DataCamp","https://www.datacamp.com/courses/cybersecurity-fundamentals")],
    [("ServiceNow","GRC Engineering Intern","Remote","https://www.servicenow.com/careers"),
     ("RSA Security","Risk Management Intern","Hybrid","https://www.rsa.com/careers"),
     ("MetricStream","Compliance Engineering Intern","On-site","https://www.metricstream.com/careers")])

append_skill("Penetration Testing",
    [("Penetration Testing","Udemy","https://www.udemy.com/course/learn-penetration-testing-from-scratch"),
     ("Ethical Hacking","Pluralsight","https://www.pluralsight.com/courses/ethical-hacking-understanding"),
     ("OSCP Preparation","Coursera","https://www.coursera.org/learn/penetration-testing"),
     ("Advanced Penetration Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/penetration-testing"),
     ("Bug Bounty Hunting","DataCamp","https://www.datacamp.com/courses/penetration-testing")],
    [("HackerOne","Bug Bounty Intern","Remote","https://www.hackerone.com/careers"),
     ("Bugcrowd","Security Engineering Intern","Hybrid","https://www.bugcrowd.com/careers"),
     ("Synack","Penetration Testing Intern","On-site","https://www.synack.com/careers")])

append_skill("Security Policies",
    [("Security Policy Development","Udemy","https://www.udemy.com/course/security-policy-development"),
     ("GRC and Compliance","Pluralsight","https://www.pluralsight.com/courses/cyber-risk-management"),
     ("NIST Cybersecurity Framework","Coursera","https://www.coursera.org/learn/nist-cybersecurity-framework"),
     ("ISO 27001 Implementation","LinkedIn Learning","https://www.linkedin.com/learning/topics/compliance"),
     ("Security Governance","DataCamp","https://www.datacamp.com/courses/cybersecurity-fundamentals")],
    [("Coalfire","Compliance Engineering Intern","Remote","https://www.coalfire.com/careers"),
     ("A-LIGN","Audit Engineering Intern","Hybrid","https://a-lign.com/careers"),
     ("Bishop Fox","Security Consulting Intern","On-site","https://www.bishopfox.com/careers")])

print("Part 2 appended successfully")
