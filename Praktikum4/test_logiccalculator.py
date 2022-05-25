from logiccalculator import LogicCalculator

# aufgabe 14
lc = LogicCalculator("((A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C))")
lc.drawKb()

# aufgabe 15
lc = LogicCalculator("(A&C) -> (B|D)")
lc.tell("(A&C) <-> (B|D)")
lc.tell("(A->C) <-> (B->D)")

lc.tell("(A&D) | (C->D)")
lc.tell("(D->C) & A")
lc.drawKb()

# aufgabe 16
# This is how to create a Model
# TTFT and TTTT works
# https://web.stanford.edu/class/cs103/tools/truth-table-tool/
# ((A&&C) -> (B||D)) && ((A&&C) <-> (B||D)) && ((A->C) <-> (B->D)) && ((A&&D) || (C->D)) && ((D->C) && A)
v = {"A": True, "B": False, "C": True, "D": True}
print(lc.pl_true(v))

#aufgabe 17
symbols = ["A", "B", "C", "D"]
symbols.reverse()
lc.test_all_symbols(symbols, {})

#aufgabe 18
print(lc.tt_entails("(A & B & C & D) | (A & -B & C & D)"))