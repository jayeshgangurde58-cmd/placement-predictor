#!/usr/bin/env python3
"""Append remaining engineering skills."""

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

# Embedded Systems
append_skill("Microcontrollers",
    [("Arduino Programming","Udemy","https://www.udemy.com/course/arduino-programming"),
     ("STM32 Microcontrollers","Pluralsight","https://www.pluralsight.com/courses/stm32-fundamentals"),
     ("Embedded C for Microcontrollers","Coursera","https://www.coursera.org/learn/embedded-systems"),
     ("PIC Microcontrollers","LinkedIn Learning","https://www.linkedin.com/learning/topics/microcontrollers"),
     ("Raspberry Pi Programming","DataCamp","https://www.datacamp.com/courses/embedded-systems")],
    [("Arduino","Embedded Engineering Intern","Remote","https://www.arduino.cc/careers"),
     ("STMicroelectronics","MCU Engineering Intern","Hybrid","https://www.st.com/careers"),
     ("Microchip","Embedded Systems Intern","On-site","https://www.microchip.com/careers")])

append_skill("RTOS",
    [("FreeRTOS Fundamentals","Udemy","https://www.udemy.com/course/freertos-fundamentals"),
     ("Real-Time Operating Systems","Pluralsight","https://www.pluralsight.com/courses/rtos-fundamentals"),
     ("RTOS for Embedded Systems","Coursera","https://www.coursera.org/learn/embedded-systems"),
     ("Zephyr RTOS","LinkedIn Learning","https://www.linkedin.com/learning/topics/rtos"),
     ("VxWorks Development","DataCamp","https://www.datacamp.com/courses/rtos")],
    [("Wind River","RTOS Engineering Intern","Remote","https://www.windriver.com/careers"),
     ("Zephyr Project","Embedded Engineering Intern","Hybrid","https://zephyrproject.org"),
     ("Amazon FreeRTOS","IoT Engineering Intern","On-site","https://www.amazon.jobs")])

append_skill("Hardware Design",
    [("Digital Electronics","Udemy","https://www.udemy.com/course/digital-electronics"),
     ("VHDL and FPGA Design","Pluralsight","https://www.pluralsight.com/courses/fpga-fundamentals"),
     ("ASIC Design","Coursera","https://www.coursera.org/learn/vlsi-cad-part1"),
     ("Verilog HDL","LinkedIn Learning","https://www.linkedin.com/learning/topics/hardware-design"),
     ("SystemVerilog","DataCamp","https://www.datacamp.com/courses/hardware-design")],
    [("AMD","Hardware Engineering Intern","Remote","https://www.amd.com/careers"),
     ("Intel","SoC Design Intern","Hybrid","https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"),
     ("NVIDIA","ASIC Engineering Intern","On-site","https://www.nvidia.com/en-us/about-nvidia/careers")])

append_skill("PCB Design",
    [("PCB Design with KiCad","Udemy","https://www.udemy.com/course/pcb-design-with-kicad"),
     ("Altium Designer","Pluralsight","https://www.pluralsight.com/courses/altium-designer-fundamentals"),
     ("Eagle PCB Design","Coursera","https://www.coursera.org/learn/electronics"),
     ("PCB Layout","LinkedIn Learning","https://www.linkedin.com/learning/topics/pcb-design"),
     ("High-Speed PCB Design","DataCamp","https://www.datacamp.com/courses/pcb-design")],
    [("Altium","PCB Engineering Intern","Remote","https://www.altium.com/careers"),
     ("Cadence","IC Design Intern","Hybrid","https://www.cadence.com/careers"),
     ("Siemens EDA","PCB Engineering Intern","On-site","https://www.sw.siemens.com/careers")])

append_skill("Signal Processing",
    [("Digital Signal Processing","Udemy","https://www.udemy.com/course/digital-signal-processing"),
     ("DSP with MATLAB","Pluralsight","https://www.pluralsight.com/courses/digital-signal-processing"),
     ("Audio Signal Processing","Coursera","https://www.coursera.org/learn/audio-signal-processing"),
     ("Image Processing","LinkedIn Learning","https://www.linkedin.com/learning/topics/signal-processing"),
     ("FFT and Spectral Analysis","DataCamp","https://www.datacamp.com/courses/signal-processing")],
    [("Shure","Audio Engineering Intern","Remote","https://www.shure.com/careers"),
     ("Bose","Signal Processing Intern","Hybrid","https://www.bose.com/careers"),
     ("Dolby","Audio R&D Intern","On-site","https://www.dolby.com/careers")])

append_skill("Firmware",
    [("Firmware Development","Udemy","https://www.udemy.com/course/firmware-development"),
     ("Embedded Firmware","Pluralsight","https://www.pluralsight.com/courses/embedded-firmware"),
     ("Bare Metal Programming","Coursera","https://www.coursera.org/learn/embedded-systems"),
     ("UEFI Development","LinkedIn Learning","https://www.linkedin.com/learning/topics/firmware"),
     ("Device Drivers","DataCamp","https://www.datacamp.com/courses/firmware")],
    [("Apple","Firmware Engineering Intern","Remote","https://jobs.apple.com"),
     ("Western Digital","Firmware Engineering Intern","Hybrid","https://jobs.westerndigital.com"),
     ("Seagate","Storage Firmware Intern","On-site","https://www.seagate.com/careers")])

append_skill("Debugging",
    [("Debugging Techniques","Udemy","https://www.udemy.com/course/debugging-techniques"),
     ("JTAG and SWD Debugging","Pluralsight","https://www.pluralsight.com/courses/debugging-embedded"),
     ("GDB Debugging","Coursera","https://www.coursera.org/learn/c-programming"),
     ("Oscilloscope Debugging","LinkedIn Learning","https://www.linkedin.com/learning/topics/debugging"),
     ("Logic Analyzer","DataCamp","https://www.datacamp.com/courses/debugging")],
    [("Segger","Debug Tool Engineering Intern","Remote","https://www.segger.com/careers"),
     ("Lauterbach","Debugging Intern","Hybrid","https://www.lauterbach.com/careers"),
     ("Total Phase","Hardware Debugging Intern","On-site","https://www.totalphase.com/careers")])

# Electrical Engineering
append_skill("Circuit Design",
    [("Circuit Analysis","Udemy","https://www.udemy.com/course/circuit-analysis"),
     ("Analog Circuit Design","Pluralsight","https://www.pluralsight.com/courses/analog-circuit-design"),
     ("Power Electronics","Coursera","https://www.coursera.org/learn/power-electronics"),
     ("RF Circuit Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/circuit-design"),
     ("PCB Circuit Design","DataCamp","https://www.datacamp.com/courses/circuit-design")],
    [("Texas Instruments","Analog Engineering Intern","Remote","https://careers.ti.com"),
     ("Analog Devices","Circuit Design Intern","Hybrid","https://www.analog.com/careers"),
     ("Maxim Integrated","Electrical Engineering Intern","On-site","https://www.maximintegrated.com/careers")])

append_skill("Electronics",
    [("Electronics Fundamentals","Udemy","https://www.udemy.com/course/electronics-fundamentals"),
     ("Electronic Circuits","Pluralsight","https://www.pluralsight.com/courses/electronics-fundamentals"),
     ("Semiconductor Devices","Coursera","https://www.coursera.org/learn/semiconductor-devices"),
     ("Power Electronics","LinkedIn Learning","https://www.linkedin.com/learning/topics/electronics"),
     ("EMC and EMI","DataCamp","https://www.datacamp.com/courses/electronics")],
    [("ON Semiconductor","Device Engineering Intern","Remote","https://www.onsemi.com/careers"),
     ("NXP Semiconductors","Electronics Intern","Hybrid","https://www.nxp.com/careers"),
     ("Infineon","Power Electronics Intern","On-site","https://www.infineon.com/careers")])

append_skill("Power Systems",
    [("Power System Analysis","Udemy","https://www.udemy.com/course/power-system-analysis"),
     ("Electrical Power Systems","Pluralsight","https://www.pluralsight.com/courses/power-systems-fundamentals"),
     ("Smart Grid","Coursera","https://www.coursera.org/learn/smart-grid"),
     ("Renewable Energy Systems","LinkedIn Learning","https://www.linkedin.com/learning/topics/power-systems"),
     ("Power Distribution","DataCamp","https://www.datacamp.com/courses/power-systems")],
    [("Siemens Energy","Power Engineering Intern","Remote","https://www.siemens-energy.com/careers"),
     ("GE Vernova","Grid Solutions Intern","Hybrid","https://www.ge.com/careers"),
     ("ABB","Power Systems Intern","On-site","https://new.abb.com/careers")])

append_skill("Matlab",
    [("MATLAB Fundamentals","Udemy","https://www.udemy.com/course/matlab-fundamentals"),
     ("MATLAB for Engineers","Pluralsight","https://www.pluralsight.com/courses/matlab-fundamentals"),
     ("Simulink for Control Systems","Coursera","https://www.coursera.org/learn/matlab"),
     ("MATLAB for Data Analysis","LinkedIn Learning","https://www.linkedin.com/learning/topics/matlab"),
     ("Advanced MATLAB","DataCamp","https://www.datacamp.com/courses/matlab")],
    [("MathWorks","MATLAB Engineering Intern","Remote","https://www.mathworks.com/company/jobs"),
     ("Boeing","Engineering Analysis Intern","Hybrid","https://jobs.boeing.com"),
     ("Northrop Grumman","Systems Engineering Intern","On-site","https://www.northropgrumman.com/careers")])

append_skill("Control Systems",
    [("Control Systems Engineering","Udemy","https://www.udemy.com/course/control-systems-engineering"),
     ("PID Controller Design","Pluralsight","https://www.pluralsight.com/courses/control-systems-fundamentals"),
     ("State Space Control","Coursera","https://www.coursera.org/learn/dynamics-control"),
     ("Robust Control","LinkedIn Learning","https://www.linkedin.com/learning/topics/control-systems"),
     ("Model Predictive Control","DataCamp","https://www.datacamp.com/courses/control-systems")],
    [("Tesla","Control Systems Intern","Remote","https://www.tesla.com/careers"),
     ("SpaceX","GNC Engineering Intern","Hybrid","https://www.spacex.com/careers"),
     ("Boston Dynamics","Controls Engineering Intern","On-site","https://www.bostondynamics.com/careers")])

append_skill("Instrumentation",
    [("Industrial Instrumentation","Udemy","https://www.udemy.com/course/industrial-instrumentation"),
     ("Process Control Instrumentation","Pluralsight","https://www.pluralsight.com/courses/instrumentation-fundamentals"),
     ("SCADA Systems","Coursera","https://www.coursera.org/learn/process-control"),
     ("PLC Programming","LinkedIn Learning","https://www.linkedin.com/learning/topics/instrumentation"),
     ("HART Protocol","DataCamp","https://www.datacamp.com/courses/instrumentation")],
    [("Honeywell","Instrumentation Engineering Intern","Remote","https://careers.honeywell.com"),
     ("Emerson","Automation Engineering Intern","Hybrid","https://www.emerson.com/careers"),
     ("Yokogawa","Instrumentation Intern","On-site","https://www.yokogawa.com/careers")])

# Electronics Engineering
append_skill("Digital Electronics",
    [("Digital Logic Design","Udemy","https://www.udemy.com/course/digital-logic-design"),
     ("FPGA Design","Pluralsight","https://www.pluralsight.com/courses/fpga-fundamentals"),
     ("VLSI Design","Coursera","https://www.coursera.org/learn/vlsi-cad-part1"),
     ("Digital IC Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/digital-electronics"),
     ("Verilog and VHDL","DataCamp","https://www.datacamp.com/courses/digital-electronics")],
    [("Xilinx","Digital Design Intern","Remote","https://www.xilinx.com/careers"),
     ("Lattice Semiconductor","FPGA Engineering Intern","Hybrid","https://www.latticesemi.com/careers"),
     ("Microchip","Digital IC Intern","On-site","https://www.microchip.com/careers")])

append_skill("Analog Circuits",
    [("Analog Circuit Design","Udemy","https://www.udemy.com/course/analog-circuit-design"),
     ("Op-Amp Circuits","Pluralsight","https://www.pluralsight.com/courses/analog-circuit-design"),
     ("Mixed-Signal Design","Coursera","https://www.coursera.org/learn/analog-circuits"),
     ("RF and Microwave","LinkedIn Learning","https://www.linkedin.com/learning/topics/analog-circuits"),
     ("ADC and DAC Design","DataCamp","https://www.datacamp.com/courses/analog-circuits")],
    [("Skyworks","Analog Engineering Intern","Remote","https://www.skyworksinc.com/careers"),
     ("Qorvo","RF Engineering Intern","Hybrid","https://www.qorvo.com/careers"),
     ("Broadcom","Mixed-Signal Intern","On-site","https://www.broadcom.com/careers")])

append_skill("PCB Layout",
    [("PCB Layout Fundamentals","Udemy","https://www.udemy.com/course/pcb-layout-fundamentals"),
     ("High-Speed PCB Layout","Pluralsight","https://www.pluralsight.com/courses/pcb-layout"),
     ("Multi-Layer PCB Design","Coursera","https://www.coursera.org/learn/electronics"),
     ("EMC PCB Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/pcb-layout"),
     ("Flex PCB Design","DataCamp","https://www.datacamp.com/courses/pcb-layout")],
    [("Sanmina","PCB Manufacturing Intern","Remote","https://www.sanmina.com/careers"),
     ("TTM Technologies","PCB Engineering Intern","Hybrid","https://www.ttm.com/careers"),
     ("Unimicron","PCB Design Intern","On-site","https://www.unimicron.com")])

append_skill("Semiconductors",
    [("Semiconductor Physics","Udemy","https://www.udemy.com/course/semiconductor-physics"),
     ("CMOS Design","Pluralsight","https://www.pluralsight.com/courses/cmos-design"),
     ("Semiconductor Manufacturing","Coursera","https://www.coursera.org/learn/semiconductor-devices"),
     ("Process Integration","LinkedIn Learning","https://www.linkedin.com/learning/topics/semiconductors"),
     ("Yield Engineering","DataCamp","https://www.datacamp.com/courses/semiconductors")],
    [("TSMC","Process Engineering Intern","Remote","https://www.tsmc.com/careers"),
     ("Samsung Foundry","Semiconductor Intern","Hybrid","https://www.samsung.com/careers"),
     ("GlobalFoundries","Manufacturing Intern","On-site","https://gf.com/careers")])

# Mechanical Engineering
append_skill("CAD",
    [("AutoCAD Fundamentals","Udemy","https://www.udemy.com/course/autocad-fundamentals"),
     ("SolidWorks Essentials","Pluralsight","https://www.pluralsight.com/courses/solidworks-essentials"),
     ("CATIA V5","Coursera","https://www.coursera.org/learn/cad-design"),
     ("Fusion 360","LinkedIn Learning","https://www.linkedin.com/learning/topics/cad"),
     ("Inventor Professional","DataCamp","https://www.datacamp.com/courses/cad")],
    [("Autodesk","CAD Engineering Intern","Remote","https://www.autodesk.com/careers"),
     ("Dassault Systemes","PLM Engineering Intern","Hybrid","https://www.3ds.com/careers"),
     ("PTC","Creo Engineering Intern","On-site","https://www.ptc.com/careers")])

append_skill("SolidWorks",
    [("SolidWorks Complete Course","Udemy","https://www.udemy.com/course/solidworks-complete-course"),
     ("SolidWorks Simulation","Pluralsight","https://www.pluralsight.com/courses/solidworks-simulation"),
     ("SolidWorks Assembly Design","Coursera","https://www.coursera.org/learn/cad-design"),
     ("Sheet Metal Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/solidworks"),
     ("SolidWorks PDM","DataCamp","https://www.datacamp.com/courses/solidworks")],
    [("SolidWorks","Software Engineering Intern","Remote","https://www.solidworks.com/careers"),
     ("Fisher Unitech","Design Engineering Intern","Hybrid","https://www.fisherunitech.com/careers"),
     ("GoEngineer","Technical Support Intern","On-site","https://www.goengineer.com/careers")])

append_skill("Thermodynamics",
    [("Thermodynamics Fundamentals","Udemy","https://www.udemy.com/course/thermodynamics-fundamentals"),
     ("Heat Transfer","Pluralsight","https://www.pluralsight.com/courses/heat-transfer"),
     ("CFD for Thermal Analysis","Coursera","https://www.coursera.org/learn/thermodynamics"),
     ("HVAC Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/thermodynamics"),
     ("Combustion Engineering","DataCamp","https://www.datacamp.com/courses/thermodynamics")],
    [("Carrier","HVAC Engineering Intern","Remote","https://www.carrier.com/careers"),
     ("Trane","Thermal Engineering Intern","Hybrid","https://www.trane.com/careers"),
     ("Lennox","Refrigeration Intern","On-site","https://www.lennox.com/careers")])

append_skill("Material Science",
    [("Materials Science","Udemy","https://www.udemy.com/course/materials-science"),
     ("Metallurgy Fundamentals","Pluralsight","https://www.pluralsight.com/courses/metallurgy-fundamentals"),
     ("Composite Materials","Coursera","https://www.coursera.org/learn/materials-science"),
     ("Nanomaterials","LinkedIn Learning","https://www.linkedin.com/learning/topics/materials-science"),
     ("Polymer Science","DataCamp","https://www.datacamp.com/courses/materials-science")],
    [("BASF","Materials Science Intern","Remote","https://www.basf.com/careers"),
     ("Dow Chemical","R&D Engineering Intern","Hybrid","https://www.dow.com/careers"),
     ("3M","Materials Engineering Intern","On-site","https://www.3m.com/careers")])

append_skill("Manufacturing",
    [("Manufacturing Processes","Udemy","https://www.udemy.com/course/manufacturing-processes"),
     ("CNC Programming","Pluralsight","https://www.pluralsight.com/courses/cnc-programming"),
     ("Lean Manufacturing","Coursera","https://www.coursera.org/learn/lean-manufacturing"),
     ("Additive Manufacturing","LinkedIn Learning","https://www.linkedin.com/learning/topics/manufacturing"),
     ("Quality in Manufacturing","DataCamp","https://www.datacamp.com/courses/manufacturing")],
    [("Tesla","Manufacturing Engineering Intern","Remote","https://www.tesla.com/careers"),
     ("Boeing","Manufacturing Intern","Hybrid","https://jobs.boeing.com"),
     ("Protolabs","Rapid Manufacturing Intern","On-site","https://www.protolabs.com/careers")])

append_skill("Mechanics",
    [("Engineering Mechanics","Udemy","https://www.udemy.com/course/engineering-mechanics"),
     ("Statics and Dynamics","Pluralsight","https://www.pluralsight.com/courses/engineering-mechanics"),
     ("Fluid Mechanics","Coursera","https://www.coursera.org/learn/fluid-mechanics"),
     ("Strength of Materials","LinkedIn Learning","https://www.linkedin.com/learning/topics/mechanics"),
     ("Vibrations","DataCamp","https://www.datacamp.com/courses/mechanics")],
    [("Lockheed Martin","Structural Engineering Intern","Remote","https://www.lockheedmartin.com/careers"),
     ("Raytheon","Mechanical Engineering Intern","Hybrid","https://www.rtx.com/careers"),
     ("General Dynamics","Engineering Intern","On-site","https://www.gd.com/careers")])

append_skill("ANSYS",
    [("ANSYS Workbench","Udemy","https://www.udemy.com/course/ansys-workbench"),
     ("ANSYS Fluent","Pluralsight","https://www.pluralsight.com/courses/ansys-fluent"),
     ("FEA with ANSYS","Coursera","https://www.coursera.org/learn/finite-element-method"),
     ("ANSYS Mechanical","LinkedIn Learning","https://www.linkedin.com/learning/topics/ansys"),
     ("ANSYS CFD","DataCamp","https://www.datacamp.com/courses/ansys")],
    [("ANSYS","Simulation Engineering Intern","Remote","https://www.ansys.com/careers"),
     ("Siemens Digital Industries","Simcenter Intern","Hybrid","https://www.sw.siemens.com/careers"),
     ("Altair","CAE Engineering Intern","On-site","https://www.altair.com/careers")])

append_skill("Product Design",
    [("Product Design Fundamentals","Udemy","https://www.udemy.com/course/product-design-fundamentals"),
     ("Design for Manufacturing","Pluralsight","https://www.pluralsight.com/courses/design-for-manufacturing"),
     ("Industrial Design","Coursera","https://www.coursera.org/learn/product-design"),
     ("Human-Centered Design","LinkedIn Learning","https://www.linkedin.com/learning/topics/product-design"),
     ("Design Thinking","DataCamp","https://www.datacamp.com/courses/product-design")],
    [("IDEO","Design Thinking Intern","Remote","https://www.ideo.com/careers"),
     ("Frog Design","Product Design Intern","Hybrid","https://www.frogdesign.com/careers"),
     ("Ammunition","Industrial Design Intern","On-site","https://ammunitiondesign.com/careers")])

print("Part 4 appended successfully")
