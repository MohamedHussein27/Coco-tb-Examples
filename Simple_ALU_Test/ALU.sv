module ALU (A,B,clk,opcode,areset,C,N_flag,arith_flag,carry_flag,logic_flag);
    input [3:0] A,B;
    input [2:0] opcode;
    input clk,areset;
    output reg [7:0]C;
    output reg N_flag,arith_flag,carry_flag,logic_flag;

    always @(posedge clk or negedge areset) begin
        if (!areset) begin
            C<=0;
            N_flag<=0;
            arith_flag<=0;
            logic_flag<=0;
            carry_flag<=0;
        end
        else begin
            case (opcode)
                //addition
                0:begin {carry_flag,C} <= A+B; arith_flag<=1; logic_flag<=0; N_flag<=0; end
                //subtraction  
                1:begin {N_flag,C} <= A-B; arith_flag<=1; logic_flag<=0; carry_flag<=0; end
                //multiplication
                2:begin C <= A*B; arith_flag<=1; logic_flag<=0; N_flag<=0; carry_flag<=0; end
                //anding 
                3:begin C <= A&B; arith_flag<=0; logic_flag<=1; N_flag<=0; carry_flag<=0; end
                //oring
                4:begin C <= A|B; arith_flag<=0; logic_flag<=1; N_flag<=0; carry_flag<=0; end
                //xoring
                5:begin C <= A^B; arith_flag<=0; logic_flag<=1; N_flag<=0; carry_flag<=0; end
                default: begin C <= C; arith_flag<=arith_flag; carry_flag<=carry_flag; N_flag<=N_flag; logic_flag<=logic_flag; end
            endcase
        end
    end
    // to create the waveform
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, ALU);
    end
endmodule