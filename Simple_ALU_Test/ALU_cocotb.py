import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.result import *


    ####start the test values###
#first test the reset
async def areset_test(dut):
    cocotb.log.info('Reset test Started')
    # driving signals
    dut.areset.value = 0
    dut.A.value = 5
    dut.B.value = 3
    dut.opcode.value = 2
    # expected outputs
    expected_C = 0
    expected_arith_flag = 0
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0
    await Timer(1, units="ns")  # Wait for the reset to take effect
    if (dut.C.value == expected_C and dut.arith_flag.value == expected_arith_flag 
        and dut.logic_flag.value == expected_logic_flag and dut.N_flag.value == expected_N_flag
        and dut.carry_flag.value == expected_carry_flag):

        cocotb.log.info('reset test passed')
    else:
        raise TestFailure('result of reset test is not correct ')
    #assert dut.C.value == expected_C, f"reset failed: {dut.C.value} != {expected_C}"
    await Timer(5, units="ns")  # Wait for a short time to ensure stability
    cocotb.log.info('reset test ended')
    dut.areset.value = 1  # Deactivate reset
    

#second check the addition
async def addition_test(dut):
    cocotb.log.info('Addition test Started')
    # driving signals
    dut.A.value = 4
    dut.B.value = 6
    dut.opcode.value = 0
    # expected outputs
    expected_C = 10
    expected_arith_flag = 1
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0

    await FallingEdge(dut.clk)  # Wait for a falling clock edge
    cocotb.log.info("outputs has the new values after the rising edge")
    #await Timer(1, units="ns")  # Wait for the reset to take effect
    if (dut.C.value == expected_C and dut.arith_flag.value == expected_arith_flag 
        and dut.logic_flag.value == expected_logic_flag and dut.N_flag.value == expected_N_flag
        and dut.carry_flag.value == expected_carry_flag):

        cocotb.log.info('Addition test passed')
    else:
        raise TestFailure('result of Addition test is not correct ')    
    #await RisingEdge(dut.clk) 
    


#third check the subtraction
async def subtraction_test(dut):
    cocotb.log.info('Subtraction test Started')
    # driving stimulus
    dut.A.value = 10
    dut.B.value = 4
    dut.opcode.value = 1
    # expected outputs
    expected_C = 6
    expected_arith_flag = 1
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0

    await FallingEdge(dut.clk)  # Wait for a falling clock edge
    cocotb.log.info("outputs has the new values after the rising edge")
    #await Timer(1, units="ns")  # Wait for the reset to take effect
    if (dut.C.value == expected_C and dut.arith_flag.value == expected_arith_flag 
        and dut.logic_flag.value == expected_logic_flag and dut.N_flag.value == expected_N_flag
        and dut.carry_flag.value == expected_carry_flag):

        cocotb.log.info('Subtraction test passed')
    else:
        raise TestFailure('result of Subtraction test is not correct ')    
    #await RisingEdge(dut.clk) 

#fourth check the AND operation
async def and_test(dut):
    cocotb.log.info('AND test Started')
    # driving signals
    dut.A.value = 6  # 0110 in binary
    dut.B.value = 3  # 0011 in binary
    dut.opcode.value = 3
    # expected outputs
    expected_C = 2  # 0010 in binary
    expected_arith_flag = 0
    expected_logic_flag = 1
    expected_N_flag = 0
    expected_carry_flag = 0

    await FallingEdge(dut.clk)  # Wait for a falling clock edge
    cocotb.log.info("outputs has the new values after the rising edge")
    #await Timer(1, units="ns")  # Wait for the reset to take effect
    if (dut.C.value == expected_C and dut.arith_flag.value == expected_arith_flag 
        and dut.logic_flag.value == expected_logic_flag and dut.N_flag.value == expected_N_flag
        and dut.carry_flag.value == expected_carry_flag):

        cocotb.log.info('AND test passed')
    else:
        raise TestFailure('result of AND test is not correct ')    
    #await RisingEdge(dut.clk) 

#fifth check the OR operation
async def or_test(dut):
    cocotb.log.info('OR test Started')
    # driving signals
    dut.A.value = 6  # 0110 in binary
    dut.B.value = 3  # 0011 in binary
    dut.opcode.value = 4
    # expected outputs
    expected_C = 7  # 0111 in binary
    expected_arith_flag = 0
    expected_logic_flag = 1
    expected_N_flag = 0
    expected_carry_flag = 0

    await FallingEdge(dut.clk)  # Wait for a falling clock edge
    cocotb.log.info("outputs has the new values after the rising edge")
    #await Timer(1, units="ns")  # Wait for the reset to take effect
    if (dut.C.value == expected_C and dut.arith_flag.value == expected_arith_flag 
        and dut.logic_flag.value == expected_logic_flag and dut.N_flag.value == expected_N_flag
        and dut.carry_flag.value == expected_carry_flag):

        cocotb.log.info('OR test passed')
    else:
        raise TestFailure('result of OR test is not correct ')    
    #await RisingEdge(dut.clk)


@cocotb.test()
async def ALU_top(dut):
    cocotb.log.info("Starting ALU test...")
    
    # clock generation
    clock = Clock(dut.clk, 10, units="ns")  # 10 ns clock period
    cocotb.start_soon(clock.start())

    # Run the tests in sequence
    await cocotb.start_soon(areset_test(dut))
    await cocotb.start_soon(addition_test(dut))
    await cocotb.start_soon(subtraction_test(dut))
    await cocotb.start_soon(and_test(dut))
    await cocotb.start_soon(or_test(dut))