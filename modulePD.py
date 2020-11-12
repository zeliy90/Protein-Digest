#print if missed cleveage is 0 or 1 or 2
#when set range give option that they dont need to
#maybe make dictionary of peptide and weight or length
    #so only print lengths that are 5 to 6
    #or print petide with weight (['AAA',5])
#aa to the left and right of peptide
    #list out seq and color code the peptides
#fix position
##
class protein_digest:
    def __init__(self,seq='',peptides=[]):
        self.seq=seq
        self.peptides=[]

    def read(self,file1):
        self.seq=''.join(open(file1).read().split())

    def trypsin(self,missed_cleavage):
        cleavages=[]
        #peptides=[]
        cut=[0]
        length=len(self.seq)
        for i in range(0,length-1):
            if self.seq[i]=='K' and self.seq[i+1]!='P':
                cut.append(i+1)
            elif self.seq[i]=='R' and self.seq[i+1]!='P':
                cut.append(i+1) 
        if cut[-1]!=length:
            cut.append(length)
        if len(cut)>2:
            if missed_cleavage==0:
                for c in range(0,len(cut)-1):
                    a=self.seq[cut[c]:cut[c+1]]
                    peptides.append(a)
                    clea=((a),0)
                    self.cleavages.append(clea)
            elif missed_cleavage==1:
                for c in range(0,len(cut)-2):
                    a=self.seq[cut[c]:cut[c+1]]
                    peptides.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self.seq[cut[c]:cut[c+2]]
                    peptides.append(b)
                    clea=((b),1)
                    self.cleavages.append(clea)
                z=self.seq[cut[-2]:cut[-1]]    
                peptides.append(z)
                clea=((z),0)
                self.cleavages.append(clea)
            elif missed_cleavage==2:
                for c in range (0,len(cut)-3):
                    a=self.seq[cut[c]:cut[c+1]]
                    peptides.append(a)
                    clea=((a),0)
                    self.cleavages.append(clea)
                    b=self.seq[cut[c]:cut[c+2]]
                    peptides.append(b)
                    clea=((b),1)
                    self.cleavages.append(clea)
                    c=self.seq[cut[c]:cut[c+3]]
                    peptides.append(c)
                    clea=((c),2)
                    self.cleavages.append(clea)     
                z=self.seq[cut[-3]:cut[-2]]
                y=self.seq[cut[-3]:cut[-1]]
                x=self.seq[cut[-2]:cut[-1]]
                peptide.append(z)
                clea=((z),2)
                self.cleavages.append(clea)
                peptide.append(y)
                clea=((y),1)
                self.cleavages.append(clea)
                peptide.append(x)
                clea=((x),0)
                self.cleavages.append(clea)
        else:
            peptides.append(self.seq)
            self.cleavages.append(self.seq)
        #return cleavages
    #might not want to use cleavage 2
    #print(trypsin('TKTPRTPTK',2))

    def pepsin(self,missed_cleavage):
        cleavages=[]
        peptide=[]
        cut=[0]
        length=len(self)            
        for i in range(0,length-1):
            if self[i]=='F':
                cut.append(i+1)
            elif self[i]=='L':
                cut.append(i+1)
            elif self[i]=='W':
                cut.append(i+1)
            elif self[i]=='Y':
                cut.append(i+1)
            elif self[i]=='A':
                cut.append(i+1)
            elif self[i]=='E':
                cut.append(i+1)
            elif self[i]=='Q':
                cut.append(i+1)
        if cut[-1]!=length:
            cut.append(length)
        if len(cut)>2:
            if missed_cleavage==0:
                for c in range(0,len(cut)-1):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
            elif missed_cleavage==1:
                for c in range(0,len(cut)-2):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                z=self[cut[-2]:cut[-1]]    
                peptide.append(z)
                clea=((z),0)
                cleavages.append(clea)
            elif missed_cleavage==2:
                for c in range (0,len(cut)-3):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                    c=self[cut[c]:cut[c+3]]
                    peptide.append(c)
                    clea=((c),2)
                    cleavages.append(clea)     
                z=self[cut[-3]:cut[-2]]
                y=self[cut[-3]:cut[-1]]
                x=self[cut[-2]:cut[-1]]
                peptide.append(z)
                clea=((z),2)
                cleavages.append(clea)
                peptide.append(y)
                clea=((y),1)
                cleavages.append(clea)
                peptide.append(x)
                clea=((x),0)
                cleavages.append(clea)
        else:
            peptides.append(self)
        return cleavages

    def argC(self,missed_cleavage):
        cleavages=[]
        peptide=[]
        cut=[0]
        length=len(self)
        for i in range(0,length-1):
            if self[i]=='R' and self[i+1]!='P':
                cut.append(i+1)
        if cut[-1]!=length:
            cut.append(length)
        if len(cut)>2:
            if missed_cleavage==0:
                for c in range(0,len(cut)-1):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
            elif missed_cleavage==1:
                for c in range(0,len(cut)-2):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                z=self[cut[-2]:cut[-1]]    
                peptide.append(z)
                clea=((z),0)
                cleavages.append(clea)
            elif missed_cleavage==2:
                for c in range (0,len(cut)-3):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                    c=self[cut[c]:cut[c+3]]
                    peptide.append(c)
                    clea=((c),2)
                    cleavages.append(clea)     
                z=self[cut[-3]:cut[-2]]
                y=self[cut[-3]:cut[-1]]
                x=self[cut[-2]:cut[-1]]
                peptide.append(z)
                clea=((z),2)
                cleavages.append(clea)
                peptide.append(y)
                clea=((y),1)
                cleavages.append(clea)
                peptide.append(x)
                clea=((x),0)
                cleavages.append(clea)
        else:
            peptides.append(self)
        return cleavages

    def aspN(self,missed_cleavage):
        cleavages=[]
        peptide=[]
        cut=[0]
        length=len(self)        
        for i in range(0,length-1):
            if self[i]=='D':
                cut.append(i+1)
        if cut[-1]!=length:
            cut.append(length)
        if len(cut)>2:
            if missed_cleavage==0:
                for c in range(0,len(cut)-1):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
            elif missed_cleavage==1:
                for c in range(0,len(cut)-2):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                z=self[cut[-2]:cut[-1]]    
                peptide.append(z)
                clea=((z),0)
                cleavages.append(clea)
            elif missed_cleavage==2:
                for c in range (0,len(cut)-3):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                    c=self[cut[c]:cut[c+3]]
                    peptide.append(c)
                    clea=((c),2)
                    cleavages.append(clea)     
                z=self[cut[-3]:cut[-2]]
                y=self[cut[-3]:cut[-1]]
                x=self[cut[-2]:cut[-1]]
                peptide.append(z)
                clea=((z),2)
                cleavages.append(clea)
                peptide.append(y)
                clea=((y),1)
                cleavages.append(clea)
                peptide.append(x)
                clea=((x),0)
                cleavages.append(clea)
        else:
            peptides.append(self)
        return cleavages

    def glucC(self,missed_cleavage):
        cleavages=[]
        peptide=[]
        cut=[0]
        length=len(self)
        for i in range(0,length-1):
            if self[i]=='E' and self[i+1]!='E'or'P':
                cut.append(i+1)
        if cut[-1]!=length:
            cut.append(length)  
        if len(cut)>2:
            if missed_cleavage==0:
                for c in range(0,len(cut)-1):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
            elif missed_cleavage==1:
                for c in range(0,len(cut)-2):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                z=self[cut[-2]:cut[-1]]    
                peptide.append(z)
                clea=((z),0)
                cleavages.append(clea)
            elif missed_cleavage==2:
                for c in range (0,len(cut)-3):
                    a=self[cut[c]:cut[c+1]]
                    peptide.append(a)
                    clea=((a),0)
                    cleavages.append(clea)
                    b=self[cut[c]:cut[c+2]]
                    peptide.append(b)
                    clea=((b),1)
                    cleavages.append(clea)
                    c=self[cut[c]:cut[c+3]]
                    peptide.append(c)
                    clea=((c),2)
                    cleavages.append(clea)     
                z=self[cut[-3]:cut[-2]]
                y=self[cut[-3]:cut[-1]]
                x=self[cut[-2]:cut[-1]]
                peptide.append(z)
                clea=((z),2)
                cleavages.append(clea)
                peptide.append(y)
                clea=((y),1)
                cleavages.append(clea)
                peptide.append(x)
                clea=((x),0)
                cleavages.append(clea)
        else:
            peptides.append(self)
        return cleavages

    def position(self):
        return [[(self.index(pep)+1,(self.index(pep)+len(pep))),pep] for pep in self]
#print(position(['ATYU','AAA']))
    def length(self):
        lenpep=[]
        for pep in self:
            lenpep=[len(pep)]
        return [[len(pep),pep] for pep in self]
    def molmass(self):
        mass=[]
        molmasses={'A':71.03711,'R':156.10111,'N':114.04293,'D':115.02694,'G':57.02146,'I':113.08406,
             'L': 113.08406,'P':97.05276,'V':99.06841,'F':147.06841,'W':186.07931,'Y':163.06333,
             'E':129.04259,'H':137.05891,'K':128.09496,'S':87.03203,'T':101.04768,'C':103.00919,'M':131.04049,
             'Q':128.05858}
        for i in self:
                mass=sum(molmasses[aa] for aa in i)+18

        return [sum(molmasses[aa] for aa in i)for i in self]
    ##        for x in lenpep:
    ##            if x>=minL and x<=maxL:
    ##                p=x,pep
    ##            else:
    ##                p='None of the peptide lengths are with in that range


    ##def peplength(peptides,maxL,minL):
    ###max and min set the range
    ##    maxL=argv.sys[1]
    ##    minL=argv.sys[2]
    ##    if maxL>minL:
    ##        for i in peptides:
    ##            maxL==len(i)
    ##            minL==len(i)
    ##            return peptides
    ####    elif maxL=None or minL=None:
    ####        return peptides
    ####    else:
    ##        return print('max length is greater then min length')

        #monoisotopic
    #peptides=['AAA','ATWV']
    
        


    def weightrange(list1,minw,maxw):
        
        for x in list1:
            if minw>=l and maxw<=r:
                print(x)
        return


