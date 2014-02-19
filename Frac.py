from fractions import Fraction

Numerator=raw_input("What's the numerator")
Denominator=raw_input("what's the Denominator")

Top=int(Numerator)
Bottom=int(Denominator)

Final=Fraction(Top,Bottom)
print(Final)