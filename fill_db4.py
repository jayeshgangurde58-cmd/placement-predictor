#!/usr/bin/env python3
"""Append final skills and close database."""

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

# Civil Engineering
append_skill("Structural Analysis",
    [("Structural Analysis Fundamentals","Udemy","https://www.udemy.com/course/structural-analysis"),
     ("Finite Element Method","Pluralsight","https://www.pluralsight.com/courses/finite-element-method"),
     ("Structural Dynamics","Coursera","https://www.coursera.org/learn/structural-mechanics"),
     ("Bridge Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/structural-analysis"),
     ("Seismic Design","DataCamp","https://www.datacamp.com/courses/structural-analysis")],
    [("AECOM","Structural Engineering Intern","Remote","https://aecom.com/careers"),
     ("Arup","Structural Design Intern","Hybrid","https://www.arup.com/careers"),
     ("WSP","Engineering Intern","On-site","https://www.wsp.com/careers")])

append_skill("AutoCAD",
    [("AutoCAD Complete Course","Udemy","https://www.udemy.com/course/autocad-complete-course"),
     ("AutoCAD Civil 3D","Pluralsight","https://www.pluralsight.com/courses/autocad-civil-3d"),
     ("Revit Architecture","Coursera","https://www.coursera.org/learn/revit"),
     ("BIM Fundamentals","LinkedIn Learning","https://www.linkedin.com/learning/topics/autocad"),
     ("Civil 3D Design","DataCamp","https://www.datacamp.com/courses/autocad")],
    [("Autodesk","Software Engineering Intern","Remote","https://www.autodesk.com/careers"),
     ("Bentley Systems","Infrastructure Intern","Hybrid","https://www.bentley.com/careers"),
     ("Trimble","Construction Tech Intern","On-site","https://www.trimble.com/careers")])

append_skill("Building Design",
    [("Architectural Design","Udemy","https://www.udemy.com/course/architectural-design"),
     ("Sustainable Building Design","Pluralsight","https://www.pluralsight.com/courses/sustainable-design"),
     ("Green Building LEED","Coursera","https://www.coursera.org/learn/sustainable-buildings"),
     ("MEP Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/building-design"),
     ("Facade Engineering","DataCamp","https://www.datacamp.com/courses/building-design")],
    [("Gensler","Architecture Intern","Remote","https://www.gensler.com/careers"),
     ("HOK","Design Intern","Hybrid","https://www.hok.com/careers"),
     ("Skidmore Owings & Merrill","Structural Intern","On-site","https://www.som.com/careers")])

append_skill("Material Strength",
    [("Mechanics of Materials","Udemy","https://www.udemy.com/course/mechanics-of-materials"),
     ("Strength of Materials","Pluralsight","https://www.pluralsight.com/courses/strength-of-materials"),
     ("Fracture Mechanics","Coursera","https://www.coursera.org/learn/solid-mechanics"),
     ("Composite Structures","LinkedIn Learning","https://www.linkedin.com/learning/topics/materials"),
     ("Concrete Design","DataCamp","https://www.datacamp.com/courses/materials")],
    [("LafargeHolcim","Materials Engineering Intern","Remote","https://www.lafargeholcim.com/careers"),
     ("CEMEX","R&D Engineering Intern","Hybrid","https://www.cemex.com/careers"),
     ("Martin Marietta","Aggregates Intern","On-site","https://www.martinmarietta.com/careers")])

append_skill("Construction Management",
    [("Construction Management","Udemy","https://www.udemy.com/course/construction-management"),
     ("Project Management for Construction","Pluralsight","https://www.pluralsight.com/courses/construction-management"),
     ("BIM in Construction","Coursera","https://www.coursera.org/learn/construction-management"),
     ("Lean Construction","LinkedIn Learning","https://www.linkedin.com/learning/topics/construction-management"),
     ("Cost Estimation","DataCamp","https://www.datacamp.com/courses/construction-management")],
    [("Turner Construction","Project Management Intern","Remote","https://www.turnerconstruction.com/careers"),
     ("Bechtel","Construction Intern","Hybrid","https://www.bechtel.com/careers"),
     ("Fluor","Engineering Intern","On-site","https://www.fluor.com/careers")])

append_skill("Surveying",
    [("Land Surveying","Udemy","https://www.udemy.com/course/land-surveying"),
     ("GPS and GNSS","Pluralsight","https://www.pluralsight.com/courses/gps-fundamentals"),
     ("Remote Sensing","Coursera","https://www.coursera.org/learn/remote-sensing"),
     ("LiDAR Technology","LinkedIn Learning","https://www.linkedin.com/learning/topics/surveying"),
     ("GIS Fundamentals","DataCamp","https://www.datacamp.com/courses/surveying")],
    [("Trimble","Surveying Engineering Intern","Remote","https://www.trimble.com/careers"),
     ("Topcon","Geospatial Intern","Hybrid","https://www.topconpositioning.com/careers"),
     ("Leica Geosystems","Measurement Intern","On-site","https://leica-geosystems.com/careers")])

append_skill("Project Planning",
    [("Construction Planning","Udemy","https://www.udemy.com/course/construction-planning"),
     ("Primavera P6","Pluralsight","https://www.pluralsight.com/courses/primavera-p6"),
     ("Microsoft Project","Coursera","https://www.coursera.org/learn/project-management"),
     ("Schedule Optimization","LinkedIn Learning","https://www.linkedin.com/learning/topics/project-planning"),
     ("Critical Path Method","DataCamp","https://www.datacamp.com/courses/project-planning")],
    [("Oracle","Construction Tech Intern","Remote","https://www.oracle.com/careers"),
     ("Procore","Product Engineering Intern","Hybrid","https://www.procore.com/careers"),
     ("PlanGrid","Software Engineering Intern","On-site","https://www.plangrid.com/careers")])

# Chemical Engineering
append_skill("Process Design",
    [("Process Design Fundamentals","Udemy","https://www.udemy.com/course/process-design"),
     ("Chemical Process Simulation","Pluralsight","https://www.pluralsight.com/courses/process-simulation"),
     ("Aspen HYSYS","Coursera","https://www.coursera.org/learn/chemical-engineering"),
     ("P&ID Development","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-design"),
     ("HAZOP Analysis","DataCamp","https://www.datacamp.com/courses/process-design")],
    [("AspenTech","Process Engineering Intern","Remote","https://www.aspentech.com/careers"),
     ("Honeywell UOP","Process Tech Intern","Hybrid","https://careers.honeywell.com"),
     ("Siemens Energy","Process Engineering Intern","On-site","https://www.siemens-energy.com/careers")])

append_skill("Heat Transfer",
    [("Heat Transfer Fundamentals","Udemy","https://www.udemy.com/course/heat-transfer"),
     ("Thermal Engineering","Pluralsight","https://www.pluralsight.com/courses/thermal-engineering"),
     ("Heat Exchanger Design","Coursera","https://www.coursera.org/learn/heat-transfer"),
     ("Boiling and Condensation","LinkedIn Learning","https://www.linkedin.com/learning/topics/heat-transfer"),
     ("Radiation Heat Transfer","DataCamp","https://www.datacamp.com/courses/heat-transfer")],
    [("Alfa Laval","Heat Transfer Intern","Remote","https://www.alfalaval.com/careers"),
     ("GEA Group","Thermal Engineering Intern","Hybrid","https://www.gea.com/careers"),
     ("SPX Flow","Process Engineering Intern","On-site","https://www.spxflow.com/careers")])

append_skill("Fluid Mechanics",
    [("Fluid Mechanics Fundamentals","Udemy","https://www.udemy.com/course/fluid-mechanics"),
     ("CFD Simulation","Pluralsight","https://www.pluralsight.com/courses/cfd-simulation"),
     ("Turbomachinery","Coursera","https://www.coursera.org/learn/fluid-mechanics"),
     ("Multiphase Flow","LinkedIn Learning","https://www.linkedin.com/learning/topics/fluid-mechanics"),
     ("Aerodynamics","DataCamp","https://www.datacamp.com/courses/fluid-mechanics")],
    [("ANSYS","CFD Engineering Intern","Remote","https://www.ansys.com/careers"),
     ("Siemens","Simcenter Engineering Intern","Hybrid","https://www.siemens.com/careers"),
     ("Dassault Systemes","Fluid Simulation Intern","On-site","https://www.3ds.com/careers")])

append_skill("Chemical Thermodynamics",
    [("Chemical Thermodynamics","Udemy","https://www.udemy.com/course/chemical-thermodynamics"),
     ("Phase Equilibria","Pluralsight","https://www.pluralsight.com/courses/thermodynamics"),
     ("Reaction Kinetics","Coursera","https://www.coursera.org/learn/chemical-kinetics"),
     ("Statistical Thermodynamics","LinkedIn Learning","https://www.linkedin.com/learning/topics/thermodynamics"),
     ("Electrochemistry","DataCamp","https://www.datacamp.com/courses/thermodynamics")],
    [("ExxonMobil","Chemical Engineering Intern","Remote","https://corporate.exxonmobil.com/careers"),
     ("Shell","Process Engineering Intern","Hybrid","https://www.shell.com/careers"),
     ("Chevron","Refining Engineering Intern","On-site","https://www.chevron.com/careers")])

append_skill("Materials",
    [("Materials Engineering","Udemy","https://www.udemy.com/course/materials-engineering"),
     ("Polymer Engineering","Pluralsight","https://www.pluralsight.com/courses/polymer-engineering"),
     ("Corrosion Engineering","Coursera","https://www.coursera.org/learn/materials-science"),
     ("Nanotechnology","LinkedIn Learning","https://www.linkedin.com/learning/topics/materials"),
     ("Biomaterials","DataCamp","https://www.datacamp.com/courses/materials")],
    [("DuPont","Materials Science Intern","Remote","https://www.dupont.com/careers"),
     ("BASF","Chemical Engineering Intern","Hybrid","https://www.basf.com/careers"),
     ("Celanese","Materials Engineering Intern","On-site","https://www.celanese.com/careers")])

append_skill("Safety",
    [("Process Safety Management","Udemy","https://www.udemy.com/course/process-safety-management"),
     ("Hazardous Area Classification","Pluralsight","https://www.pluralsight.com/courses/process-safety"),
     ("Functional Safety IEC 61511","Coursera","https://www.coursera.org/learn/process-safety"),
     ("PSM Compliance","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-safety"),
     ("LOPA and SIL","DataCamp","https://www.datacamp.com/courses/process-safety")],
    [("Process Safety Solutions","Safety Engineering Intern","Remote","https://www.processsafety.com"),
     ("ioMosaic","Risk Analysis Intern","Hybrid","https://www.iomosaic.com/careers"),
     ("AECom","HSE Engineering Intern","On-site","https://aecom.com/careers")])

append_skill("Reaction Engineering",
    [("Chemical Reaction Engineering","Udemy","https://www.udemy.com/course/chemical-reaction-engineering"),
     ("Catalyst Design","Pluralsight","https://www.pluralsight.com/courses/reaction-engineering"),
     ("Reactor Design","Coursera","https://www.coursera.org/learn/chemical-kinetics"),
     ("Bioreactor Engineering","LinkedIn Learning","https://www.linkedin.com/learning/topics/reaction-engineering"),
     ("Combustion Engineering","DataCamp","https://www.datacamp.com/courses/reaction-engineering")],
    [("Johnson Matthey","Catalyst Engineering Intern","Remote","https://matthey.com/careers"),
     ("BASF","Chemical Engineering Intern","Hybrid","https://www.basf.com/careers"),
     ("Clariant","Process Development Intern","On-site","https://www.clariant.com/careers")])

append_skill("Simulation",
    [("Process Simulation","Udemy","https://www.udemy.com/course/process-simulation"),
     ("Aspen Plus","Pluralsight","https://www.pluralsight.com/courses/aspen-plus"),
     ("COMSOL Multiphysics","Coursera","https://www.coursera.org/learn/multiphysics-simulation"),
     ("gPROMS Modeling","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-simulation"),
     ("MATLAB Simulation","DataCamp","https://www.datacamp.com/courses/simulation")],
    [("AspenTech","Simulation Engineering Intern","Remote","https://www.aspentech.com/careers"),
     ("Siemens","Process Simulation Intern","Hybrid","https://www.siemens.com/careers"),
     ("PSE","Modeling Engineering Intern","On-site","https://www.psenterprise.com/careers")])

# Industrial Engineering
append_skill("Process Improvement",
    [("Lean Six Sigma","Udemy","https://www.udemy.com/course/lean-six-sigma"),
     ("Kaizen Principles","Pluralsight","https://www.pluralsight.com/courses/kaizen-principles"),
     ("Value Stream Mapping","Coursera","https://www.coursera.org/learn/lean-manufacturing"),
     ("5S Methodology","LinkedIn Learning","https://www.linkedin.com/learning/topics/process-improvement"),
     ("Continuous Improvement","DataCamp","https://www.datacamp.com/courses/process-improvement")],
    [("Toyota","Process Improvement Intern","Remote","https://www.toyota.com/careers"),
     ("Boeing","Industrial Engineering Intern","Hybrid","https://jobs.boeing.com"),
     ("Amazon","Operations Engineering Intern","On-site","https://www.amazon.jobs")])

append_skill("Lean Manufacturing",
    [("Lean Manufacturing Principles","Udemy","https://www.udemy.com/course/lean-manufacturing"),
     ("Toyota Production System","Pluralsight","https://www.pluralsight.com/courses/lean-manufacturing"),
     ("Just-in-Time","Coursera","https://www.coursera.org/learn/lean-manufacturing"),
     ("Kanban System","LinkedIn Learning","https://www.linkedin.com/learning/topics/lean-manufacturing"),
     ("Pull Production","DataCamp","https://www.datacamp.com/courses/lean-manufacturing")],
    [("Toyota","Lean Manufacturing Intern","Remote","https://www.toyota.com/careers"),
     ("GE Aerospace","Manufacturing Intern","Hybrid","https://www.geaerospace.com/careers"),
     ("John Deere","Operations Intern","On-site","https://www.deere.com/careers")])

append_skill("Six Sigma",
    [("Six Sigma Green Belt","Udemy","https://www.udemy.com/course/six-sigma-green-belt"),
     ("Six Sigma Black Belt","Pluralsight","https://www.pluralsight.com/courses/six-sigma-black-belt"),
     ("DMAIC Methodology","Coursera","https://www.coursera.org/learn/six-sigma"),
     ("Statistical Process Control","LinkedIn Learning","https://www.linkedin.com/learning/topics/six-sigma"),
     ("Design for Six Sigma","DataCamp","https://www.datacamp.com/courses/six-sigma")],
    [("Motorola Solutions","Quality Engineering Intern","Remote","https://www.motorolasolutions.com/careers"),
     ("3M","Six Sigma Intern","Hybrid","https://www.3m.com/careers"),
     ("Honeywell","Quality Intern","On-site","https://careers.honeywell.com")])

append_skill("Operations Research",
    [("Operations Research","Udemy","https://www.udemy.com/course/operations-research"),
     ("Linear Programming","Pluralsight","https://www.pluralsight.com/courses/optimization-fundamentals"),
     ("Queueing Theory","Coursera","https://www.coursera.org/learn/operations-research"),
     ("Integer Programming","LinkedIn Learning","https://www.linkedin.com/learning/topics/operations-research"),
     ("Simulation Modeling","DataCamp","https://www.datacamp.com/courses/operations-research")],
    [("McKinsey","Operations Research Intern","Remote","https://www.mckinsey.com/careers"),
     ("Bain & Company","Analytics Intern","Hybrid","https://www.bain.com/careers"),
     ("BCG","Data Science Intern","On-site","https://www.bcg.com/careers")])

append_skill("Supply Chain",
    [("Supply Chain Management","Udemy","https://www.udemy.com/course/supply-chain-management"),
     ("Logistics and Distribution","Pluralsight","https://www.pluralsight.com/courses/supply-chain-fundamentals"),
     ("Inventory Management","Coursera","https://www.coursera.org/learn/supply-chain-management"),
     ("Demand Planning","LinkedIn Learning","https://www.linkedin.com/learning/topics/supply-chain"),
     ("Warehouse Management","DataCamp","https://www.datacamp.com/courses/supply-chain")],
    [("Amazon","Supply Chain Intern","Remote","https://www.amazon.jobs"),
     ("DHL","Logistics Intern","Hybrid","https://www.dhl.com/careers"),
     ("FedEx","Operations Research Intern","On-site","https://careers.fedex.com")])

append_skill("Quality Control",
    [("Statistical Quality Control","Udemy","https://www.udemy.com/course/statistical-quality-control"),
     ("ISO 9001","Pluralsight","https://www.pluralsight.com/courses/quality-management"),
