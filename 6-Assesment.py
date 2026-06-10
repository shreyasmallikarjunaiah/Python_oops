class Bacterium:
    def __init__(self,shape,feature,color,cel_wall):
        self.shape=shape
        self.feature=feature
        self.color=color
        self.cel_wall=cel_wall



Escherichia_coli=Bacterium("circular","gut","red","thin")
Streptococcus_pneumoniae=Bacterium("cylindrical","pneumonia ","blue","Hard")
Staphylococcus_aureus=Bacterium("cone","lungs","yello","smooth")
Salmonella_enterica=Bacterium("pipe","eyes","purple","thin")
Helicobacter_pylori=Bacterium("semi_circle","legs","black","spongy")



Bacterias={"Escherichia_coli":Escherichia_coli,"Streptococcus_pneumoniae":Streptococcus_pneumoniae,"Staphylococcus_aureus":Staphylococcus_aureus,"Salmonella_enterica":Salmonella_enterica,"Helicobacter_pylori":Helicobacter_pylori}
names=input("Enter the name of the Bacterium to know more:")

if names in Bacterias:
    a=Bacterias[names]
    print(a.shape,a.feature,a.color,a.cel_wall)

#
# class Bacterium:
#     def __init__(self, shape, feature, color, cel_wall):
#         self.shape = shape
#         self.feature = feature
#         self.color = color
#         self.cel_wall = cel_wall
#
#
# Escherichia_coli = Bacterium("circular", "gut", "red", "thin")
# Streptococcus_pneumoniae = Bacterium("cylindrical", "pneumonia", "blue", "hard")
# Staphylococcus_aureus = Bacterium("cone", "lungs", "yellow", "smooth")
# Salmonella_enterica = Bacterium("pipe", "eyes", "purple", "thin")
# Helicobacter_pylori = Bacterium("semi_circle", "legs", "black", "spongy")
#
# # Dictionary mapping names to objects
# Bacterias = {
#     "Escherichia_coli": Escherichia_coli,
#     "Streptococcus_pneumoniae": Streptococcus_pneumoniae,
#     "Staphylococcus_aureus": Staphylococcus_aureus,
#     "Salmonella_enterica": Salmonella_enterica,
#     "Helicobacter_pylori": Helicobacter_pylori
# }
#
# Name = input("Enter the name of the Bacterium to know more: ")
#
# if Name in Bacterias:
#     b = Bacterias[Name]
#     print(b.shape, b.feature, b.color, b.cel_wall)
# else:
#     print("Bacterium not found")