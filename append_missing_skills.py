#!/usr/bin/env python3
"""Append missing skills to course_database.py and fix syntax."""

import os

OUT = "backend/services/course_database.py"

def append_skill(name, courses, internships):
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

# ===== GENERAL =====
append_skill("Networking",
    [("Computer Networking Fundamentals","Udemy","https://www.udemy.com/course/computer-networking-fundamentals"),
     ("Networking Essentials","Coursera","https://www.coursera.org/specializations/computer-communications"),
     ("Network+ Certification","Pluralsight","https://www.pluralsight.com/paths/comptia-network-plus"),
     ("Cisco Networking Basics","LinkedIn Learning","https://www.linkedin.com/learning/topics/networking"),
     ("Software-Defined Networking","DataCamp","https://www.datacamp.com/courses/networking-fundamentals")],
    [("Cisco","Network Engineering Intern","Remote","https://jobs.cisco.com"),
     ("Juniper Networks","Networking Intern","Hybrid","https://www.juniper.net/careers"),
     ("Arista Networks","Network Engineering Intern","On-site","https://www.arista.com/careers")])

append_skill("Embedded Systems",
    [("Introduction to Embedded Systems","Coursera","https://www.coursera.org/learn/embedded-systems"),
     ("Embedded Systems Programming","Udemy","https://www.udemy.com/course/embedded-systems-programming"),
     ("ARM Cortex-M Programming","Pluralsight","https://www.pluralsight.com/courses/embedded-systems-arm"),
     ("Real-Time Embedded Systems","LinkedIn Learning","https://www.linkedin.com/learning/topics/embedded-systems"),
     ("IoT and Embedded Systems","DataCamp","https://www.datacamp.com/courses/embedded-systems")],
    [("ARM","Embedded Engineering Intern","Remote","https://www.arm.com/careers"),
     ("NXP","Embedded Systems Intern","Hybrid","https://www.nxp.com/careers"),
     ("Renesas","MCU Engineering Intern","On-site","https://www.renesas.com/careers")])

append_skill("Data Analysis",
    [("Data Analysis with Python","Coursera","https://www.coursera.org/learn/data-analysis-with-python"),
     ("Data Analyst Bootcamp","Udemy","https://www.udemy.com/course/data-analyst-bootcamp"),
     ("SQL for Data Analysis","Pluralsight","https://www.pluralsight.com/courses/sql-data-analysis"),
     ("Excel for Data Analysis","LinkedIn Learning","https://www.linkedin.com/learning/topics/data-analysis"),
     ("Business Analytics","DataCamp","https://www.datacamp.com/courses/data-analysis")],
    [("Accenture","Data Analyst Intern","Remote","https://www.accenture.com/careers"),
     ("Deloitte","Analytics Intern","Hybrid","https://www.deloitte.com/careers"),
     ("McKinsey","Data Analyst Intern","On-site","https://www.mckinsey.com/careers")])

# ===== CIVIL ENGINEERING =====
append_skill("Structural Analysis",
    [("Structural Analysis Fundamentals","Udemy","https://www.udemy.com/course/structural-analysis"),
     ("Structural Engineering","Coursera","https://www.coursera.org/learn/structural-engineering"),
     ("Finite Element Analysis","Pluralsight","https://www.pluralsight.com/courses/finite-element-analysis"),
     ("Structural Dynamics","LinkedIn Learning","https://www.linkedin.com/learning/topics/structural-analysis"),
     ("Seismic Design","DataCamp","https://www.datacamp.com/courses/structural-analysis")],
    [("Arup","Structural Engineering Intern","Remote","https://www.arup.com/careers"),
     ("AECOM","Structural Intern","Hybrid","https://aecom.com/careers"),
     ("WSP","Structural Engineering Intern","On-site","https://www.wsp.com/careers")])

append_skill("Building Design",
    [("Building Design and Construction","Udemy","https://www.udemy.com/course/building-design"),
     ("Architectural Design","Coursera","https://www.coursera.org/learn/architectural-design"),
     ("BIM for Building Design","Pluralsight","https://www.pluralsight.com/courses/bim-fundamentals"),
     ("Sustainable Building Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/building-design"),
     ("Green Building Certification","DataCamp","https://www.datacamp.com/courses/building-design")],
    [("Gensler","Building Design Intern","Remote","https://www.gensler.com/careers"),
     ("HOK","Architectural Intern","Hybrid","https://www.hok.com/careers"),
     ("SOM","Design Intern","On-site","https://www.som.com/careers")])

append_skill("Material Strength",
    [("Strength of Materials","Udemy","https://www.udemy.com/course/strength-of-materials"),
     ("Mechanics of Materials","Coursera","https://www.coursera.org/learn/mechanics-of-materials"),
     ("Material Failure Analysis","Pluralsight","https://www.pluralsight.com/courses/material-failure-analysis"),
     ("Fracture Mechanics","LinkedIn Learning","https://www.linkedin.com/learning/topics/materials-engineering"),
     ("Fatigue Analysis","DataCamp","https://www.datacamp.com/courses/materials-engineering")],
    [("Bechtel","Materials Engineering Intern","Remote","https://www.bechtel.com/careers"),
     ("Fluor","Engineering Intern","Hybrid","https://www.fluor.com/careers"),
     ("Jacobs","Materials Intern","On-site","https://www.jacobs.com/careers")])

append_skill("Construction Management",
    [("Construction Management Fundamentals","Udemy","https://www.udemy.com/course/construction-management"),
     ("Construction Project Management","Coursera","https://www.coursera.org/learn/construction-management"),
     ("BIM for Construction","Pluralsight","https://www.pluralsight.com/courses/bim-construction"),
     ("Lean Construction","LinkedIn Learning","https://www.linkedin.com/learning/topics/construction-management"),
     ("Cost Estimation","DataCamp","https://www.datacamp.com/courses/construction-management")],
    [("Turner Construction","Project Management Intern","Remote","https://www.turnerconstruction.com/careers"),
     ("Skanska","Construction Intern","Hybrid","https://www.skanska.com/careers"),
     ("Kiewit","Field Operations Intern","On-site","https://www.kiewit.com/careers")])

append_skill("Surveying",
    [("Land Surveying Fundamentals","Udemy","https://www.udemy.com/course/land-surveying"),
     ("Geomatics Engineering","Coursera","https://www.coursera.org/learn/geomatics"),
     ("GPS and GNSS Surveying","Pluralsight","https://www.pluralsight.com/courses/gps-surveying"),
     ("Total Station Surveying","LinkedIn Learning","https://www.linkedin.com/learning/topics/surveying"),
     ("Remote Sensing","DataCamp","https://www.datacamp.com/courses/surveying")],
    [("Trimble","Surveying Intern","Remote","https://www.trimble.com/careers"),
     ("Leica Geosystems","Geomatics Intern","Hybrid","https://leica-geosystems.com/careers"),
     ("Topcon","Survey Engineering Intern","On-site","https://www.topconpositioning.com/careers")])

append_skill("Project Planning",
    [("Project Management Fundamentals","Udemy","https://www.udemy.com/course/project-management-fundamentals"),
     ("Project Planning and Control","Coursera","https://www.coursera.org/learn/project-planning"),
     ("Primavera P6","Pluralsight","https://www.pluralsight.com/courses/primavera-p6"),
     ("Microsoft Project","LinkedIn Learning","https://www.linkedin.com/learning/topics/project-planning"),
     ("Agile Project Management","DataCamp","https://www.datacamp.com/courses/project-planning")],
    [("PMI","Project Management Intern","Remote","https://www.pmi.org/careers"),
     ("Oracle","Project Planning Intern","Hybrid","https://www.oracle.com/careers"),
     ("SAP","Project Management Intern","On-site","https://jobs.sap.com")])

# ===== CHEMICAL ENGINEERING =====
append_skill("Process Design",
    [("Chemical Process Design","Udemy","https://www.udemy.com/course/chemical-process-design"),
     ("Process Engineering","Coursera","https://www.coursera.org/learn/chemical-engineering"),
     ("P&ID Development","Pluralsight","https://www.pluralsight.com/courses/process-design"),
     ("HYSYS Simulation","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-design"),
     ("Aspen Plus","DataCamp","https://www.datacamp.com/courses/process-design")],
    [("Air Products","Process Engineering Intern","Remote","https://www.airproducts.com/careers"),
     ("Linde","Process Design Intern","Hybrid","https://www.linde.com/careers"),
     ("Praxair","Chemical Engineering Intern","On-site","https://www.praxair.com/careers")])

append_skill("Heat Transfer",
    [("Heat Transfer Fundamentals","Udemy","https://www.udemy.com/course/heat-transfer"),
     ("Thermal Systems Engineering","Coursera","https://www.coursera.org/learn/thermal-systems"),
     ("CFD for Heat Transfer","Pluralsight","https://www.pluralsight.com/courses/cfd-heat-transfer"),
     ("Boiler and Heat Exchanger Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/heat-transfer"),
     ("Radiation Heat Transfer","DataCamp","https://www.datacamp.com/courses/heat-transfer")],
    [("Honeywell UOP","Process Engineering Intern","Remote","https://careers.honeywell.com"),
     ("Eastman Chemical","Chemical Engineering Intern","Hybrid","https://www.eastman.com/careers"),
     ("Celanese","Process Engineering Intern","On-site","https://www.celanese.com/careers")])

append_skill("Chemical Thermodynamics",
    [("Chemical Thermodynamics","Udemy","https://www.udemy.com/course/chemical-thermodynamics"),
     ("Thermodynamics for Chemical Engineers","Coursera","https://www.coursera.org/learn/thermodynamics"),
     ("Phase Equilibrium","Pluralsight","https://www.pluralsight.com/courses/phase-equilibrium"),
     ("Chemical Reaction Thermodynamics","LinkedIn Learning","https://www.linkedin.com/learning/topics/chemical-engineering"),
     ("Statistical Thermodynamics","DataCamp","https://www.datacamp.com/courses/chemical-engineering")],
    [("Dow","Chemical Engineering Intern","Remote","https://www.dow.com/careers"),
     ("DuPont","R&D Engineering Intern","Hybrid","https://www.dupont.com/careers"),
     ("BASF","Process Engineering Intern","On-site","https://www.basf.com/careers")])

append_skill("Safety",
    [("Process Safety Management","Udemy","https://www.udemy.com/course/process-safety-management"),
     ("Hazard and Operability Study","Coursera","https://www.coursera.org/learn/process-safety"),
     ("HAZOP and LOPA","Pluralsight","https://www.pluralsight.com/courses/hazop-analysis"),
     ("OSHA Standards","LinkedIn Learning","https://www.linkedin.com/learning/topics/occupational-safety"),
     ("Risk Assessment","DataCamp","https://www.datacamp.com/courses/safety-management")],
    [("BakerRisk","Safety Engineering Intern","Remote","https://www.bakerrisk.com/careers"),
     ("ioMosaic","Process Safety Intern","Hybrid","https://www.iomosaic.com/careers"),
     ("ABS Group","Safety Consulting Intern","On-site","https://www.abs-group.com/careers")])

append_skill("Reaction Engineering",
    [("Chemical Reaction Engineering","Udemy","https://www.udemy.com/course/chemical-reaction-engineering"),
     ("Reactor Design","Coursera","https://www.coursera.org/learn/chemical-reactors"),
     ("Catalysis and Reaction Kinetics","Pluralsight","https://www.pluralsight.com/courses/reaction-kinetics"),
     ("Biochemical Engineering","LinkedIn Learning","https://www.linkedin.com/learning/topics/reaction-engineering"),
     ("Polymer Reaction Engineering","DataCamp","https://www.datacamp.com/courses/reaction-engineering")],
    [("Cabot Corporation","Reaction Engineering Intern","Remote","https://www.cabotcorp.com/careers"),
     ("Wacker Chemie","Chemical Engineering Intern","Hybrid","https://www.wacker.com/careers"),
     ("Evonik","Process Engineering Intern","On-site","https://corporate.evonik.com/careers")])

append_skill("Simulation",
    [("Process Simulation","Udemy","https://www.udemy.com/course/process-simulation"),
     ("Aspen Plus Simulation","Coursera","https://www.coursera.org/learn/process-simulation"),
     ("CFD Simulation","Pluralsight","https://www.pluralsight.com/courses/cfd-simulation"),
     ("Discrete Event Simulation","LinkedIn Learning","https://www.linkedin.com/learning/topics/simulation"),
     ("Monte Carlo Simulation","DataCamp","https://www.datacamp.com/courses/simulation")],
    [("ANSYS","Simulation Engineering Intern","Remote","https://www.ansys.com/careers"),
     ("Siemens","Simulation Intern","Hybrid","https://www.sw.siemens.com/careers"),
     ("Altair","Simulation Engineering Intern","On-site","https://www.altair.com/careers")])

# ===== INDUSTRIAL ENGINEERING =====
append_skill("Process Improvement",
    [("Process Improvement Fundamentals","Udemy","https://www.udemy.com/course/process-improvement"),
     ("Six Sigma Green Belt","Coursera","https://www.coursera.org/specializations/six-sigma-green-belt"),
     ("Kaizen and Continuous Improvement","Pluralsight","https://www.pluralsight.com/courses/continuous-improvement"),
     ("Value Stream Mapping","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-improvement"),
     ("Root Cause Analysis","DataCamp","https://www.datacamp.com/courses/process-improvement")],
    [("McKinsey","Operations Intern","Remote","https://www.mckinsey.com/careers"),
     ("Boston Consulting Group","Process Improvement Intern","Hybrid","https://www.bcg.com/careers"),
     ("Bain","Operations Intern","On-site","https://www.bain.com/careers")])

append_skill("Six Sigma",
    [("Six Sigma Yellow Belt","Udemy","https://www.udemy.com/course/six-sigma-yellow-belt"),
     ("Six Sigma Black Belt","Coursera","https://www.coursera.org/specializations/six-sigma-black-belt"),
     ("DMAIC Methodology","Pluralsight","https://www.pluralsight.com/courses/six-sigma-dmaic"),
     ("Statistical Process Control","LinkedIn Learning","https://www.linkedin.com/learning/topics/six-sigma"),
     ("Design for Six Sigma","DataCamp","https://www.datacamp.com/courses/six-sigma")],
    [("Motorola Solutions","Six Sigma Intern","Remote","https://www.motorolasolutions.com/careers"),
     ("General Electric","Quality Engineering Intern","Hybrid","https://www.ge.com/careers"),
     ("Honeywell","Six Sigma Intern","On-site","https://careers.honeywell.com")])

append_skill("Operations Research",
    [("Operations Research Fundamentals","Udemy","https://www.udemy.com/course/operations-research"),
     ("Optimization Methods","Coursera","https://www.coursera.org/learn/optimization"),
     ("Linear Programming","Pluralsight","https://www.pluralsight.com/courses/linear-programming"),
     ("Queueing Theory","LinkedIn Learning","https://www.linkedin.com/learning/topics/operations-research"),
     ("Network Optimization","DataCamp","https://www.datacamp.com/courses/operations-research")],
    [("Amazon","Operations Research Intern","Remote","https://www.amazon.jobs"),
     ("UPS","Operations Research Intern","Hybrid","https://www.jobs-ups.com"),
     ("FedEx","Operations Intern","On-site","https://careers.fedex.com")])

append_skill("Supply Chain",
    [("Supply Chain Management","Udemy","https://www.udemy.com/course/supply-chain-management"),
     ("Supply Chain Specialization","Coursera","https://www.coursera.org/specializations/supply-chain-management"),
     ("Logistics and Distribution","Pluralsight","https://www.pluralsight.com/courses/logistics-management"),
     ("Demand Planning","LinkedIn Learning","https://www.linkedin.com/learning/topics/supply-chain"),
     ("Inventory Management","DataCamp","https://www.datacamp.com/courses/supply-chain")],
    [("DHL","Supply Chain Intern","Remote","https://www.dhl.com/careers"),
     ("Maersk","Supply Chain Intern","Hybrid","https://www.maersk.com/careers"),
     ("C.H. Robinson","Logistics Intern","On-site","https://www.chrobinson.com/careers")])

append_skill("Quality Control",
    [("Quality Control Fundamentals","Udemy","https://www.udemy.com/course/quality-control"),
     ("Statistical Quality Control","Coursera","https://www.coursera.org/learn/quality-control"),
     ("ISO 9001 Quality Management","Pluralsight","https://www.pluralsight.com/courses/iso-9001"),
     ("SPC and Control Charts","LinkedIn Learning","https://www.linkedin.com/learning/topics/quality-control"),
     ("Quality Auditing","DataCamp","https://www.datacamp.com/courses/quality-control")],
    [("Tesla","Quality Engineering Intern","Remote","https://www.tesla.com/careers"),
     ("Boeing","Quality Intern","Hybrid","https://jobs.boeing.com"),
     ("Toyota","Quality Control Intern","On-site","https://www.toyota.com/careers")])

append_skill("ERP",
    [("SAP ERP Fundamentals","Udemy","https://www.udemy.com/course/sap-erp-fundamentals"),
     ("Oracle ERP Cloud","Coursera","https://www.coursera.org/learn/oracle-erp"),
     ("Microsoft Dynamics 365","Pluralsight","https://www.pluralsight.com/courses/dynamics-365-fundamentals"),
     ("NetSuite ERP","LinkedIn Learning","https://www.linkedin.com/learning/topics/erp"),
     ("Workday HCM","DataCamp","https://www.datacamp.com/courses/erp")],
    [("SAP","ERP Consulting Intern","Remote","https://jobs.sap.com"),
     ("Oracle","ERP Implementation Intern","Hybrid","https://www.oracle.com/careers"),
     ("Microsoft","Dynamics 365 Intern","On-site","https://careers.microsoft.com")])

append_skill("Production Planning",
    [("Production Planning and Control","Udemy","https://www.udemy.com/course/production-planning"),
     ("Manufacturing Planning","Coursera","https://www.coursera.org/learn/manufacturing-planning"),
     ("MRP and ERP Planning","Pluralsight","https://www.pluralsight.com/courses/mrp-planning"),
     ("Advanced Planning and Scheduling","LinkedIn Learning","https://www.linkedin.com/learning/topics/production-planning"),
     ("Just-in-Time Manufacturing","DataCamp","https://www.datacamp.com/courses/production-planning")],
    [("Plex Systems","Production Planning Intern","Remote","https://www.plex.com/careers"),
     ("Epicor","ERP Intern","Hybrid","https://www.epicor.com/careers"),
     ("Infor","Manufacturing Intern","On-site","https://www.infor.com/careers")])

# ===== BIOMEDICAL ENGINEERING =====
append_skill("Biomaterials",
    [("Biomaterials Science","Udemy","https://www.udemy.com/course/biomaterials"),
     ("Introduction to Biomaterials","Coursera","https://www.coursera.org/learn/biomaterials"),
     ("Tissue Engineering","Pluralsight","https://www.pluralsight.com/courses/tissue-engineering"),
     ("Biocompatibility Testing","LinkedIn Learning","https://www.linkedin.com/learning/topics/biomaterials"),
     ("Implant Materials","DataCamp","https://www.datacamp.com/courses/biomaterials")],
    [("Medtronic","Biomaterials Intern","Remote","https://www.medtronic.com/careers"),
     ("Johnson & Johnson","Materials Science Intern","Hybrid","https://www.jnj.com/careers"),
     ("Stryker","Biomedical Engineering Intern","On-site","https://careers.stryker.com")])

append_skill("Medical Imaging",
    [("Medical Imaging Fundamentals","Udemy","https://www.udemy.com/course/medical-imaging"),
     ("MRI and CT Physics","Coursera","https://www.coursera.org/learn/medical-imaging"),
     ("Radiology Informatics","Pluralsight","https://www.pluralsight.com/courses/radiology-informatics"),
     ("DICOM Standards","LinkedIn Learning","https://www.linkedin.com/learning/topics/medical-imaging"),
     ("Image-Guided Surgery","DataCamp","https://www.datacamp.com/courses/medical-imaging")],
    [("GE HealthCare","Imaging Engineering Intern","Remote","https://www.gehealthcare.com/careers"),
     ("Siemens Healthineers","Medical Imaging Intern","Hybrid","https://www.siemens-healthineers.com/careers"),
     ("Philips Healthcare","Imaging Intern","On-site","https://www.philips.com/careers")])

append_skill("Biomechanics",
    [("Biomechanics Fundamentals","Udemy","https://www.udemy.com/course/biomechanics"),
     ("Musculoskeletal Biomechanics","Coursera","https://www.coursera.org/learn/biomechanics"),
     ("Motion Capture Analysis","Pluralsight","https://www.pluralsight.com/courses/motion-capture"),
     ("Gait Analysis","LinkedIn Learning","https://www.linkedin.com/learning/topics/biomechanics"),
     ("Orthopedic Biomechanics","DataCamp","https://www.datacamp.com/courses/biomechanics")],
    [("Zimmer Biomet","Biomechanics Intern","Remote","https://www.zimmerbiomet.com/careers"),
     ("DePuy Synthes","Engineering Intern","Hybrid","https://www.depuysynthes.com/careers"),
     ("Smith & Nephew","R&D Intern","On-site","https://www.smith-nephew.com/careers")])

append_skill("Regulatory Standards",
    [("FDA Regulations for Medical Devices","Udemy","https://www.udemy.com/course/fda-regulations"),
     ("ISO 13485 Quality Management","Coursera","https://www.coursera.org/learn/iso-13485"),
     ("CE Marking for Medical Devices","Pluralsight","https://www.pluralsight.com/courses/ce-marking"),
     ("21 CFR Part 820","LinkedIn Learning","https://www.linkedin.com/learning/topics/regulatory-affairs"),
     ("Clinical Trial Regulations","DataCamp","https://www.datacamp.com/courses/regulatory-affairs")],
    [("FDA","Regulatory Intern","Remote","https://www.fda.gov/jobs"),
     ("Emergo by UL","Regulatory Affairs Intern","Hybrid","https://www.emergogroup.com/careers"),
     ("NAMSA","Regulatory Consulting Intern","On-site","https://www.namsa.com/careers")])

# ===== ROBOTICS ENGINEERING =====
append_skill("Robotics",
    [("Robotics Specialization","Coursera","https://www.coursera.org/specializations/robotics"),
     ("Modern Robotics","Udemy","https://www.udemy.com/course/modern-robotics"),
     ("Robot Operating System (ROS)","Pluralsight","https://www.pluralsight.com/courses/ros-fundamentals"),
     ("Robotic Manipulators","LinkedIn Learning","https://www.linkedin.com/learning/topics/robotics"),
     ("Autonomous Robotics","DataCamp","https://www.datacamp.com/courses/robotics")],
    [("Boston Dynamics","Robotics Engineering Intern","Remote","https://www.bostondynamics.com/careers"),
     ("iRobot","Robotics Intern","Hybrid","https://www.irobot.com/careers"),
     ("Universal Robots","Robotics Engineering Intern","On-site","https://www.universal-robots.com/careers")])

append_skill("ROS",
    [("ROS for Beginners","Udemy","https://www.udemy.com/course/ros-for-beginners"),
     ("ROS Navigation Stack","Coursera","https://www.coursera.org/learn/ros-navigation"),
     ("ROS2 Fundamentals","Pluralsight","https://www.pluralsight.com/courses/ros2-fundamentals"),
     ("Gazebo Simulation","LinkedIn Learning","https://www.linkedin.com/learning/topics/ros"),
     ("MoveIt Motion Planning","DataCamp","https://www.datacamp.com/courses/ros")],
    [("Open Robotics","ROS Engineering Intern","Remote","https://www.openrobotics.org/careers"),
     ("Fetch Robotics","Robotics Intern","Hybrid","https://www.fetchrobotics.com/careers"),
     ("Locus Robotics","Robotics Engineering Intern","On-site","https://locusrobotics.com/careers")])

append_skill("Sensors",
    [("Sensor Technology","Udemy","https://www.udemy.com/course/sensor-technology"),
     ("IoT Sensors and Actuators","Coursera","https://www.coursera.org/learn/iot-sensors"),
     ("MEMS and NEMS","Pluralsight","https://www.pluralsight.com/courses/mems-sensors"),
     ("Wearable Sensors","LinkedIn Learning","https://www.linkedin.com/learning/topics/sensors"),
     ("Sensor Fusion","DataCamp","https://www.datacamp.com/courses/sensors")],
    [("Bosch Sensortec","Sensor Engineering Intern","Remote","https://www.bosch-sensortec.com/careers"),
     ("TE Connectivity","Sensor Intern","Hybrid","https://www.te.com/careers"),
     ("Amphenol","Sensor Engineering Intern","On-site","https://www.amphenol.com/careers")])

append_skill("Actuators",
    [("Actuator Design","Udemy","https://www.udemy.com/course/actuator-design"),
     ("Electric Drives","Coursera","https://www.coursera.org/learn/electric-drives"),
     ("Hydraulic and Pneumatic Systems","Pluralsight","https://www.pluralsight.com/courses/hydraulic-systems"),
     ("Servo Motor Control","LinkedIn Learning","https://www.linkedin.com/learning/topics/actuators"),
     ("Piezoelectric Actuators","DataCamp","https://www.datacamp.com/courses/actuators")],
    [("Parker Hannifin","Actuator Engineering Intern","Remote","https://www.parker.com/careers"),
     ("Moog","Motion Control Intern","Hybrid","https://www.moog.com/careers"),
     (" SMC Corporation","Actuator Engineering Intern","On-site","https://www.smcworld.com/careers")])

append_skill("Kinematics",
    [("Robot Kinematics","Udemy","https://www.udemy.com/course/robot-kinematics"),
     ("Forward and Inverse Kinematics","Coursera","https://www.coursera.org/learn/robot-kinematics"),
     ("Spatial Kinematics","Pluralsight","https://www.pluralsight.com/courses/robot-kinematics"),
     ("Jacobian and Dynamics","LinkedIn Learning","https://www.linkedin.com/learning/topics/robotics"),
     ("Trajectory Planning","DataCamp","https://www.datacamp.com/courses/robotics")],
    [("ABB Robotics","Robotics Engineering Intern","Remote","https://new.abb.com/careers"),
     ("KUKA","Robotics Intern","Hybrid","https://www.kuka.com/careers"),
     ("FANUC","Robotics Engineering Intern","On-site","https://www.fanucamerica.com/careers")])

# ===== IOT ENGINEERING =====
append_skill("Connectivity",
    [("IoT Connectivity Fundamentals","Udemy","https://www.udemy.com/course/iot-connectivity"),
     ("Wireless Communication for IoT","Coursera","https://www.coursera.org/learn/iot-connectivity"),
     ("5G and IoT","Pluralsight","https://www.pluralsight.com/courses/5g-iot"),
     ("LPWAN Technologies","LinkedIn Learning","https://www.linkedin.com/learning/topics/iot-connectivity"),
     ("Bluetooth and Zigbee","DataCamp","https://www.datacamp.com/courses/iot-connectivity")],
    [("Sierra Wireless","IoT Connectivity Intern","Remote","https://www.sierrawireless.com/careers"),
     ("Telit","IoT Engineering Intern","Hybrid","https://www.telit.com/careers"),
     ("u-blox","Connectivity Engineering Intern","On-site","https://www.u-blox.com/careers")])

append_skill("MQTT",
    [("MQTT Protocol Fundamentals","Udemy","https://www.udemy.com/course/mqtt-protocol"),
     ("IoT Messaging with MQTT","Coursera","https://www.coursera.org/learn/mqtt-iot"),
     ("MQTT Broker Setup","Pluralsight","https://www.pluralsight.com/courses/mqtt-fundamentals"),
     ("MQTT Security","LinkedIn Learning","https://www.linkedin.com/learning/topics/mqtt"),
     ("MQTT and AWS IoT","DataCamp","https://www.datacamp.com/courses/mqtt")],
    [("HiveMQ","IoT Engineering Intern","Remote","https://www.hivemq.com/careers"),
     ("Eclipse Foundation","Open Source Intern","Hybrid","https://www.eclipse.org/careers"),
     ("EMQ","MQTT Engineering Intern","On-site","https://www.emqx.io/careers")])

append_skill("Cloud Platforms",
    [("AWS IoT Core","Udemy","https://www.udemy.com/course/aws-iot-core"),
     ("Azure IoT Hub","Coursera","https://www.coursera.org/learn/azure-iot"),
     ("Google Cloud IoT","Pluralsight","https://www.pluralsight.com/courses/google-cloud-iot"),
     ("IBM Watson IoT","LinkedIn Learning","https://www.linkedin.com/learning/topics/iot-cloud"),
     ("Particle IoT Platform","DataCamp","https://www.datacamp.com/courses/iot-cloud")],
    [("Particle","IoT Platform Intern","Remote","https://www.particle.io/careers"),
     ("Blynk","IoT Engineering Intern","Hybrid","https://blynk.io/careers"),
     ("ThingWorx","IoT Development Intern","On-site","https://www.ptc.com/careers")])

append_skill("Data Analytics",
    [("IoT Data Analytics","Udemy","https://www.udemy.com/course/iot-data-analytics"),
     ("Big Data for IoT","Coursera","https://www.coursera.org/learn/iot-data-analytics"),
     ("Time Series Analysis","Pluralsight","https://www.pluralsight
