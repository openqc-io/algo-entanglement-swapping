OPENQASM 2.0;
include "qelib1.inc";
// Entanglement swapping: q[0]-q[1] and q[2]-q[3] Bell pairs
// then Bell measurement on q[1],q[2] entangles q[0] and q[3]
qreg q[4];
creg c[4];
// Create Bell pair 1: q[0] <-> q[1]
h q[0];
cx q[0],q[1];
// Create Bell pair 2: q[2] <-> q[3]
h q[2];
cx q[2],q[3];
// Bell measurement on q[1] and q[2] (intermediate node)
cx q[1],q[2];
h q[1];
measure q[1] -> c[1];
measure q[2] -> c[2];
// Apply corrections to q[3] based on measurement outcomes
if(c[2]==1) x q[3];
if(c[1]==1) z q[3];
measure q[0] -> c[0];
measure q[3] -> c[3];
