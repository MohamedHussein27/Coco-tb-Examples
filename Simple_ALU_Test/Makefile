# Set simulator
SIM ?= icarus  # You can change to: questa, vcs, modelsim, etc.

# Set language
TOPLEVEL_LANG ?= verilog  # Use vhdl for VHDL designs

# Path to design sources
PWD := $(shell pwd)
VERILOG_SOURCES := $(PWD)/ALU.sv  # Replace with your Verilog file

# Top-level design module
TOPLEVEL := ALU  # Replace with your DUT module name

# Python testbench module (test_<dut>.py → test_<dut>)
MODULE := ALU_cocotb  # Replace <dut> with the testbench name (no .py)

# Cocotb include
include $(shell cocotb-config --makefiles)/Makefile.sim
