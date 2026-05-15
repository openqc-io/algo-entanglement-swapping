"""Auto-generated template for entanglement-swapping.

Migrated to four-axis model. QASM inlined so the sandbox (no file/network
access) can execute it without reading circuit.qasm at runtime.
"""


_QASM = "OPENQASM 2.0;\ninclude \"qelib1.inc\";\n// Entanglement swapping: q[0]-q[1] and q[2]-q[3] Bell pairs\n// then Bell measurement on q[1],q[2] entangles q[0] and q[3]\nqreg q[4];\ncreg c[4];\n// Create Bell pair 1: q[0] <-> q[1]\nh q[0];\ncx q[0],q[1];\n// Create Bell pair 2: q[2] <-> q[3]\nh q[2];\ncx q[2],q[3];\n// Bell measurement on q[1] and q[2] (intermediate node)\ncx q[1],q[2];\nh q[1];\nmeasure q[1] -> c[1];\nmeasure q[2] -> c[2];\n// Apply corrections to q[3] based on measurement outcomes\nif(c[2]==1) x q[3];\nif(c[1]==1) z q[3];\nmeasure q[0] -> c[0];\nmeasure q[3] -> c[3];\n"


class AlgorithmTemplate:

    def build(self, input_data, ctx):
        return {
            "type": "circuit",
            "qasm_code": _QASM,
        }

    def interpret(self, raw_result, input_data):
        counts = raw_result.get("counts", {})
        total = sum(counts.values()) or 1
        probabilities = {state: c / total for state, c in counts.items()}
        return {
            "counts": counts,
            "probabilities": probabilities,
            "total_shots": total,
        }
