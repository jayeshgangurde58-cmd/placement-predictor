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

# Network Engineering
append_skill("TCP/IP",
    [("TCP/IP Protocol Fundamentals","Udemy","https://www.udemy.com/course/tcp-ip-fundamentals"),
     ("Networking Fundamentals","Coursera","https://www.coursera.org/specializations/computer-communications"),
     ("TCP/IP and Networking","Pluralsight","https://www.pluralsight.com/courses/tcp-ip-networking-fundamentals"),
     ("Advanced TCP/IP","LinkedIn Learning","https://www.linkedin.com/learning/topics/networking-protocols"),
     ("Wireshark and Packet Analysis","DataCamp","https://www.datacamp.com/courses/network-analysis")],
    [("Cisco","Network Engineering Intern","Remote","https://jobs.cisco.com"),
     ("Juniper Networks","Networking Intern","Hybrid","https://www.juniper.net/careers"),
     ("Arista Networks","Network Engineering Intern","On-site","https://www.arista.com/careers")])

append_skill("Routing",
    [("Routing and Switching","Udemy","https://www.udemy.com/course/routing-and-switching"),
     ("Cisco CCNA Routing","Coursera","https://www.coursera.org/learn/networking-basics"),
     ("Advanced Routing","Pluralsight","https://www.pluralsight.com/courses/routing-fundamentals"),
     ("BGP and OSPF","LinkedIn Learning","https://www.linkedin.com/learning/topics/network-routing"),
     ("Software-Defined Networking","DataCamp","https://www.datacamp.com/courses/networking-fundamentals")],
    [("Cisco","Routing Engineering Intern","Remote","https://jobs.cisco.com"),
     ("VMware","NSX Engineering Intern","Hybrid","https://careers.vmware.com"),
     ("Nokia","IP Routing Intern","On-site","https://www.nokia.com/careers")])

append_skill("Switching",
    [("LAN Switching Fundamentals","Udemy","https://www.udemy.com/course/lan-switching-fundamentals"),
     ("Cisco Switching","Pluralsight","https://www.pluralsight.com/courses/switching-fundamentals"),
     ("Network Switching","Coursera","https://www.coursera.org/learn/networking-basics"),
     ("VLAN and Trunking","LinkedIn Learning","https://www.linkedin.com/learning/topics/network-switching"),
     ("Data Center Switching","DataCamp","https://www.datacamp.com/courses/networking-fundamentals")],
    [("Cisco","Switching Engineering Intern","Remote","https://jobs.cisco.com"),
     ("Dell Technologies","Network Engineering Intern","Hybrid","https://jobs.dell.com"),
     ("HPE","Aruba Networking Intern","On-site","https://careers.hpe.com")])

append_skill("VPN",
    [("VPN Fundamentals","Udemy","https://www.udemy.com/course/vpn-fundamentals"),
     ("IPSec and SSL VPN","Pluralsight","https://www.pluralsight.com/courses/vpn-fundamentals"),
     ("WireGuard and OpenVPN","Coursera","https://www.coursera.org/learn/network-security"),
     ("Zero Trust Networking","LinkedIn Learning","https://www.linkedin.com/learning/topics/vpn"),
     ("Cloud VPN Solutions","DataCamp","https://www.datacamp.com/courses/network-security")],
    [("Cloudflare","Network Engineering Intern","Remote","https://www.cloudflare.com/careers"),
     ("Tailscale","VPN Engineering Intern","Hybrid","https://tailscale.com/careers"),
     ("Perimeter 81","Security Engineering Intern","On-site","https://www.perimeter81.com/careers")])

append_skill("Network Monitoring",
    [("Network Monitoring with Nagios","Udemy","https://www.udemy.com/course/network-monitoring"),
     ("Zabbix Monitoring","Pluralsight","https://www.pluralsight.com/courses/zabbix-monitoring"),
     ("PRTG and SNMP","Coursera","https://www.coursera.org/learn/network-management"),
     ("Network Performance Monitoring","LinkedIn Learning","https://www.linkedin.com/learning/topics/network-monitoring"),
     ("Datadog Network Monitoring","DataCamp","https://www.datacamp.com/courses/network-monitoring")],
    [("Datadog","Network Monitoring Intern","Remote","https://www.datadoghq.com/careers"),
     ("SolarWinds","Network Management Intern","Hybrid","https://www.solarwinds.com/careers"),
     ("ManageEngine","IT Operations Intern","On-site","https://www.manageengine.com/careers")])

append_skill("Troubleshooting",
    [("Network Troubleshooting","Udemy","https://www.udemy.com/course/network-troubleshooting"),
     ("IT Troubleshooting Skills","Pluralsight","https://www.pluralsight.com/courses/it-troubleshooting"),
     ("Systematic Troubleshooting","Coursera","https://www.coursera.org/learn/troubleshooting"),
     ("Advanced Troubleshooting","LinkedIn Learning","https://www.linkedin.com/learning/topics/troubleshooting"),
     ("Root Cause Analysis","DataCamp","https://www.datacamp.com/courses/troubleshooting-fundamentals")],
    [("ServiceNow","IT Operations Intern","Remote","https://www.servicenow.com/careers"),
     ("PagerDuty","Incident Management Intern","Hybrid","https://www.pagerduty.com/careers"),
     ("Opsgenie","Operations Engineering Intern","On-site","https://www.atlassian.com/software/opsgenie")])

append_skill("Wireless Networks",
    [("Wireless Networking Fundamentals","Udemy","https://www.udemy.com/course/wireless-networking-fundamentals"),
     ("Wi-Fi 6 and 6E","Pluralsight","https://www.pluralsight.com/courses/wireless-networking-fundamentals"),
     ("CWNA Certification","Coursera","https://www.coursera.org/learn/wireless-communications"),
     ("5G Networks","LinkedIn Learning","https://www.linkedin.com/learning/topics/wireless-networking"),
     ("IoT Wireless Protocols","DataCamp","https://www.datacamp.com/courses/wireless-networking")],
    [("Ubiquiti","Wireless Engineering Intern","Remote","https://www.ui.com/careers"),
     ("Cambium Networks","Wireless Engineering Intern","Hybrid","https://www.cambiumnetworks.com/careers"),
     ("Ericsson","5G Engineering Intern","On-site","https://www.ericsson.com/careers")])

append_skill("Subnetting",
    [("IP Subnetting Fundamentals","Udemy","https://www.udemy.com/course/ip-subnetting"),
     ("Subnetting Mastery","Pluralsight","https://www.pluralsight.com/courses/ip-subnetting"),
     ("IPv4 and IPv6","Coursera","https://www.coursera.org/learn/networking-basics"),
     ("Advanced Subnetting","LinkedIn Learning","https://www.linkedin.com/learning/topics/networking"),
     ("Network Addressing","DataCamp","https://www.datacamp.com/courses/networking-fundamentals")],
    [("Cisco","Network Engineering Intern","Remote","https://jobs.cisco.com"),
     ("ARIN","Network Operations Intern","Hybrid","https://www.arin.net/careers"),
     ("RIPE NCC","Internet Registry Intern","On-site","https://www.ripe.net/careers")])

append_skill("OSI Model",
    [("OSI Model Fundamentals","Udemy","https://www.udemy.com/course/osi-model"),
     ("Network Protocols","Pluralsight","https://www.pluralsight.com/courses/network-protocols-fundamentals"),
     ("Computer Networking","Coursera","https://www.coursera.org/specializations/computer-communications"),
     ("Protocol Analysis","LinkedIn Learning","https://www.linkedin.com/learning/topics/networking-protocols"),
     ("Network Architecture","DataCamp","https://www.datacamp.com/courses/networking-fundamentals")],
    [("IETF","Internet Standards Intern","Remote","https://www.ietf.org"),
     ("ICANN","Internet Governance Intern","Hybrid","https://www.icann.org/careers"),
     ("ISOC","Internet Policy Intern","On-site","https://www.internetsociety.org/careers")])

# QA Engineering
append_skill("Test Planning",
    [("Test Planning and Management","Udemy","https://www.udemy.com/course/test-planning"),
     ("Software Test Planning","Pluralsight","https://www.pluralsight.com/courses/software-test-planning"),
     ("Test Strategy","Coursera","https://www.coursera.org/learn/software-testing"),
     ("Agile Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/software-testing"),
     ("Risk-Based Testing","DataCamp","https://www.datacamp.com/courses/software-testing")],
    [("TestRail","QA Engineering Intern","Remote","https://www.gurock.com/careers"),
     ("Xray","Test Management Intern","Hybrid","https://www.getxray.app/careers"),
     ("Zephyr","Quality Engineering Intern","On-site","https://www.smartbear.com/careers")])

append_skill("Automation",
    [("Test Automation Engineering","Udemy","https://www.udemy.com/course/test-automation-engineering"),
     ("Selenium WebDriver","Pluralsight","https://www.pluralsight.com/courses/selenium-webdriver-getting-started"),
     ("Cypress Testing","Coursera","https://www.coursera.org/learn/automated-testing"),
     ("Robot Framework","LinkedIn Learning","https://www.linkedin.com/learning/topics/test-automation"),
     ("Appium Mobile Testing","DataCamp","https://www.datacamp.com/courses/test-automation")],
    [("Selenium","Open Source Intern","Remote","https://www.selenium.dev"),
     ("Cypress.io","Engineering Intern","Hybrid","https://www.cypress.io/careers"),
     ("SmartBear","Automation Engineering Intern","On-site","https://www.smartbear.com/careers")])

append_skill("Selenium",
    [("Selenium with Python","Udemy","https://www.udemy.com/course/selenium-webdriver-with-python"),
     ("Selenium WebDriver Advanced","Pluralsight","https://www.pluralsight.com/courses/selenium-webdriver-advanced"),
     ("Selenium Grid","Coursera","https://www.coursera.org/learn/automated-testing"),
     ("Selenium 4 Features","LinkedIn Learning","https://www.linkedin.com/learning/topics/selenium"),
     ("Selenium Framework Design","DataCamp","https://www.datacamp.com/courses/selenium-fundamentals")],
    [("Sauce Labs","Selenium Engineering Intern","Remote","https://saucelabs.com/company/careers"),
     ("LambdaTest","Cloud Testing Intern","Hybrid","https://www.lambdatest.com/careers"),
     ("BrowserStack","QA Engineering Intern","On-site","https://www.browserstack.com/careers")])

append_skill("JUnit",
    [("JUnit 5 Fundamentals","Udemy","https://www.udemy.com/course/junit-5-fundamentals"),
     ("Java Testing with JUnit","Pluralsight","https://www.pluralsight.com/courses/junit-5-fundamentals"),
     ("Test-Driven Development with JUnit","Coursera","https://www.coursera.org/learn/software-testing"),
     ("Mockito and JUnit","LinkedIn Learning","https://www.linkedin.com/learning/topics/junit"),
     ("Advanced JUnit","DataCamp","https://www.datacamp.com/courses/java-testing")],
    [("JetBrains","Developer Tools Intern","Remote","https://www.jetbrains.com/careers"),
     ("IntelliJ","Java Engineering Intern","Hybrid","https://www.jetbrains.com/idea"),
     ("Gradle","Build Engineering Intern","On-site","https://gradle.org/careers")])

append_skill("Performance Testing",
    [("Performance Testing with JMeter","Udemy","https://www.udemy.com/course/performance-testing-jmeter"),
     ("LoadRunner Fundamentals","Pluralsight","https://www.pluralsight.com/courses/load-testing-fundamentals"),
     ("Gatling Performance Testing","Coursera","https://www.coursera.org/learn/performance-testing"),
     ("K6 Load Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/performance-testing"),
     ("NeoLoad Advanced","DataCamp","https://www.datacamp.com/courses/performance-testing")],
    [("BlazeMeter","Performance Engineering Intern","Remote","https://www.blazemeter.com/careers"),
     ("Grafana","Observability Engineering Intern","Hybrid","https://grafana.com/careers"),
     ("LoadRunner","Performance Testing Intern","On-site","https://www.microfocus.com/careers")])

append_skill("Bug Tracking",
    [("Jira for QA","Udemy","https://www.udemy.com/course/jira-for-qa"),
     ("Bug Tracking Fundamentals","Pluralsight","https://www.pluralsight.com/courses/bug-tracking-fundamentals"),
     ("Issue Management","Coursera","https://www.coursera.org/learn/project-management"),
     ("Defect Management","LinkedIn Learning","https://www.linkedin.com/learning/topics/bug-tracking"),
     ("Quality Center","DataCamp","https://www.datacamp.com/courses/bug-tracking")],
    [("Atlassian","Jira Engineering Intern","Remote","https://www.atlassian.com/company/careers"),
     ("Monday.com","Product Engineering Intern","Hybrid","https://monday.com/careers"),
     ("Linear","Issue Tracking Intern","On-site","https://linear.app/careers")])

append_skill("API Testing",
    [("API Testing with Postman","Udemy","https://www.udemy.com/course/postman-api-testing"),
     ("REST API Testing","Pluralsight","https://www.pluralsight.com/courses/api-testing-fundamentals"),
     ("GraphQL Testing","Coursera","https://www.coursera.org/learn/api-testing"),
     ("SoapUI and REST","LinkedIn Learning","https://www.linkedin.com/learning/topics/api-testing"),
     ("Karate DSL","DataCamp","https://www.datacamp.com/courses/api-testing")],
    [("Postman","API Platform Intern","Remote","https://www.postman.com/careers"),
     ("SmartBear","API Testing Intern","Hybrid","https://www.smartbear.com/careers"),
     ("Katalon","Test Automation Intern","On-site","https://www.katalon.com/careers")])

append_skill("Manual Testing",
    [("Manual Testing Fundamentals","Udemy","https://www.udemy.com/course/manual-testing"),
     ("Exploratory Testing","Pluralsight","https://www.pluralsight.com/courses/exploratory-testing"),
     ("Usability Testing","Coursera","https://www.coursera.org/learn/user-experience-design"),
     ("Black Box Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/software-testing"),
     ("User Acceptance Testing","DataCamp","https://www.datacamp.com/courses/software-testing")],
    [("UserTesting","UX Research Intern","Remote","https://www.usertesting.com/careers"),
     ("Testlio","QA Engineering Intern","Hybrid","https://testlio.com/careers"),
     ("Applause","Crowdtesting Intern","On-site","https://www.applause.com/careers")])

append_skill("Regression Testing",
    [("Regression Testing Strategies","Udemy","https://www.udemy.com/course/regression-testing"),
     ("Test Automation for Regression","Pluralsight","https://www.pluralsight.com/courses/regression-testing"),
     ("Continuous Testing","Coursera","https://www.coursera.org/learn/continuous-testing"),
     ("Visual Regression Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/regression-testing"),
     ("Automated Regression","DataCamp","https://www.datacamp.com/courses/regression-testing")],
    [("Chromatic","Visual Testing Intern","Remote","https://www.chromatic.com/careers"),
     ("Percy","Visual Regression Intern","Hybrid","https://percy.io/careers"),
     ("BackstopJS","Testing Engineering Intern","On-site","https://github.com/garris/BackstopJS")])

# Systems Engineering
append_skill("Windows Server",
    [("Windows Server Administration","Udemy","https://www.udemy.com/course/windows-server-administration"),
     ("Active Directory Fundamentals","Pluralsight","https://www.pluralsight.com/courses/active-directory-fundamentals"),
     ("Windows Server 2022","Coursera","https://www.coursera.org/learn/windows-server-management"),
     ("PowerShell Scripting","LinkedIn Learning","https://www.linkedin.com/learning/topics/windows-server"),
     ("Azure AD Connect","DataCamp","https://www.datacamp.com/courses/windows-server")],
    [("Microsoft","Windows Engineering Intern","Remote","https://careers.microsoft.com"),
     ("VMware","Virtualization Engineering Intern","Hybrid","https://careers.vmware.com"),
     ("Citrix","Systems Engineering Intern","On-site","https://www.citrix.com/careers")])

append_skill("Scripting",
    [("Shell Scripting","Udemy","https://www.udemy.com/course/shell-scripting"),
     ("PowerShell for Sysadmins","Pluralsight","https://www.pluralsight.com/courses/powershell-for-sysadmins"),
     ("Python Scripting","Coursera","https://www.coursera.org/learn/python-scripting"),
     ("Bash Scripting","LinkedIn Learning","https://www.linkedin.com/learning/topics/shell-scripting"),
     ("Perl and Ruby Scripting","DataCamp","https://www.datacamp.com/courses/scripting")],
    [("Red Hat","Automation Engineering Intern","Remote","https://www.redhat.com/en/jobs"),
     ("Puppet","Infrastructure Engineering Intern","Hybrid","https://puppet.com/careers"),
     ("Chef","DevOps Engineering Intern","On-site","https://www.chef.io/careers")])

append_skill("Infrastructure",
    [("IT Infrastructure","Udemy","https://www.udemy.com/course/it-infrastructure"),
     ("Data Center Infrastructure","Pluralsight","https://www.pluralsight.com/courses/data-center-infrastructure"),
     ("Cloud Infrastructure","Coursera","https://www.coursera.org/learn/cloud-infrastructure"),
     ("Server Infrastructure","LinkedIn Learning","https://www.linkedin.com/learning/topics/infrastructure"),
     ("Hyperconverged Infrastructure","DataCamp","https://www.datacamp.com/courses/infrastructure")],
    [("Nutanix","Infrastructure Engineering Intern","Remote","https://www.nutanix.com/careers"),
     ("Pure Storage","Storage Engineering Intern","Hybrid","https://www.purestorage.com/careers"),
     ("NetApp","Data Management Intern","On-site","https://www.netapp.com/careers")])

append_skill("Virtualization",
    [("VMware vSphere","Udemy","https://www.udemy.com/course/vmware-vsphere"),
     ("Hyper-V Fundamentals","Pluralsight","https://www.pluralsight.com/courses/hyper-v-fundamentals"),
     ("KVM and QEMU","Coursera","https://www.coursera.org/learn/virtualization"),
     ("Proxmox VE","LinkedIn Learning","https://www.linkedin.com/learning/topics/virtualization"),
     ("VirtualBox and Vagrant","DataCamp","https://www.datacamp.com/courses/virtualization")],
    [("VMware","Virtualization Engineering Intern","Remote","https://careers.vmware.com"),
     ("Citrix","Virtual Apps Intern","Hybrid","https://www.citrix.com/careers"),
     ("Parallels","Virtualization Engineering Intern","On-site","https://www.parallels.com/careers")])

append_skill("Security",
    [("Systems Security","Udemy","https://www.udemy.com/course/systems-security"),
     ("Endpoint Security","Pluralsight","https://www.pluralsight.com/courses/endpoint-security"),
     ("Identity Management","Coursera","https://www.coursera.org/learn/identity-and-access-management"),
     ("Zero Trust Security","LinkedIn Learning","https://www.linkedin.com/learning/topics/systems-security"),
     ("SIEM and SOAR","DataCamp","https://www.datacamp.com/courses/systems-security")],
    [("CrowdStrike","Endpoint Security Intern","Remote","https://www.crowdstrike.com/careers"),
     ("SentinelOne","Security Engineering Intern","Hybrid","https://www.sentinelone.com/careers"),
     ("Cybereason","Threat Hunting Intern","On-site","https://www.cybereason.com/careers")])

print("Part 3 appended successfully")
