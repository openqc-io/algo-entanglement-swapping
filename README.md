# Entanglement Swapping

> **Category**: fundamentals &nbsp;|&nbsp; **Difficulty**: intermediate &nbsp;|&nbsp; **Qubits**: 4 &nbsp;|&nbsp; **Gates**: 10 &nbsp;|&nbsp; **Depth**: 8

Entanglement swapping extends entanglement over long distances without direct interaction. Two Bell pairs are created: (q[0],q[1]) and (q[2],q[3]). A Bell measurement on q[1] and q[2] (held by an intermediate node) projects q[0] and q[3] into an entangled Bell state, even though they never interacted. Classical communication of the measurement result allows the receiver to apply corrections. This is the basis of quantum repeaters.

## Expected Output

q[0] and q[3] in a Bell state; measurement outcomes correlated

## Circuit

The OpenQASM 2.0 circuit is in [`circuit.qasm`](./circuit.qasm).

```
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
```

## Tags

`entanglement-swapping` `quantum-repeater` `bell-measurement` `fundamentals`

## References

- [Żukowski et al. (1993). Event-ready-detectors Bell experiment via entanglement swapping. PRL 71, 4287](https://doi.org/10.1103/PhysRevLett.71.4287)

## License

MIT — part of the [OpenQC Algorithm Catalog](https://github.com/openqc-algorithms).
