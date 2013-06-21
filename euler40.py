champerowne = ""
for r in range(1,1000000):
	champerowne += str(r)
print champerowne[0], champerowne[9], champerowne[99], champerowne[999], champerowne[9999], champerowne[99999], champerowne[999999]
print int(champerowne[0])*int(champerowne[9])*int(champerowne[99])*int(champerowne[999])*int(champerowne[9999])*int(champerowne[99999])*int(champerowne[999999])
