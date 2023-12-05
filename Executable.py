#I need these modules in order for the program to compile
#Tkiner is already a preinstalled module
#You are required to install numpy_financial
from tkinter import *
from tkinter import ttk
import numpy_financial as npf
  
# Creating the tkinter window
# setting the window screen and giving it a title
master = Tk()
master.geometry("300x700")
master.title("CO1109 hkh6 cw1")
#notebook is needed to create tabs on our window
notebook = ttk.Notebook(master)

#the grid function is used and it splits the window into a grid
#labels/checkboxes/ dropboxees ect. locations are specified where they'll draw on the screen using the grid function
#the pack function is a basic version of the grid function - it just draws it underneath what was last drawn
#.get() takes what the user has inputted via user forms, checkboxes or dropboxes

# setting a frame for every tab
# This makes each tab independant from eachother i.e if an error occurs on one tab, the rest aren't affected
tab1 = Frame(notebook) 
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)
#adding the tabs to our window
notebook.add(tab1, text= "Tab 1")
notebook.add(tab2, text= "Tab 2")
notebook.add(tab3, text= "Tab 3")
notebook.add(tab4, text= "Refresh")
notebook.pack() # renders everything on the screen

#I have abosultely no idea what i am typing so im just gonna write really random things with the hope that it all works out okay


################ THE REFRESH TAB STARTS HERE, this is an extra segment:

#if the user presses the refresh tab 1, the command assosiated will wipe everything in that tab
def clear_it_1():
    #loops much like mainloop (see the end) the children attributes are destroyed
    for widget in tab1.winfo_children():
        widget.destroy()
    start()  #because the frame would be completely destroyed, we want to recall our first function to repeat the process
def clear_it_2():
    for widget in tab2.winfo_children():
        widget.destroy()
    tell()
def clear_it_3():
    for widget in tab3.winfo_children():
        widget.destroy()
    start_3()
def refresh_tab(): #This is what the user will be presented with
    #By pressing the button, the tab the button is assosiated with will be wiped (see above functions)
    labegab = Label(tab4 , text="Choose an option: ").pack()
    labebab = Label(tab4 , text=" ").pack() # this just leaves a gap between the label and the button
    yeah = Button(tab4 , text="Refresh tab 1 calculations" , command=clear_it_1).pack()
    labebab = Label(tab4 , text=" ").pack()
    yeah = Button(tab4 , text="Refresh tab 2 calculations" , command=clear_it_2).pack()
    labebab = Label(tab4 , text=" ").pack()
    yeah = Button(tab4 , text="Refresh tab 3 calculations" , command=clear_it_3).pack()
    labebab = Label(tab4 , text=" ").pack()
    #Alternatively, the user can end the program by pressing the terminate button
    nah = Button(tab4 , text="Terminate program" , command=master.destroy).pack()
    
#this part of the [program] really indicates a ton of syntax errors bound to happen
#this uses predetermined parts of the tkinter engine and they hide the complexities of the classes assosiated with it
#
        
##################### TAB 1 STARTS HERE

#Type 1 - gross margin, operating margin     
#User can enter the gross profit and sales then press continue
#the calculation function is called when the user presses continue
#Exception handling means that the program wil attempt the calculation with what the user has entered
#If its not the expected data type then the program will throw an error and the user will be prompted to change their input
#This will happen until the user has entered the correct datatype
#Calculations will occur and an output will be given
#The continue button will be disabled to functions don't loop over eachother

def gross_margin_funct():
    def calc_gromar():
        try:
            #implementing the equation, when the user inputs a value it will be in string format
            #converting the value to float to carry out the equation
            gro_mar = float(gro_pro.get())/float(sales.get())
            gro_mar_round = "{:.2f}".format(gro_mar) # to get answer to 2d.p.
            #bg highlights the output (i've chosen the colour yellow) so its very evident to the user
            labelly = Label(tab1, text="Your Gross margin: " + str(gro_mar_round) + "%" , bg='yellow').grid(row = 14 , column = 0)
            conti = Button(tab1 , text="Continue" , state=DISABLED).grid(row = 12 , column = 0)
        except ValueError: #if the wrong datatype was entered e.g. a string
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row = 8 , column = 1 , rowspan = 3)

    tabb1 = Label(tab1, text="GM - Enter gross profit here: ").grid(row = 8 , column = 0)
    #Entry creates the white square where the user can input the information prompted
    gro_pro = Entry(tab1 , width=30 , borderwidth = 5)
    gro_pro.grid(row = 9 , column = 0)

    tabb2 = Label(tab1, text="GM - Enter sales here: ").grid(row = 10 , column = 0)
    sales = Entry(tab1 , width=30 , borderwidth = 5)
    sales.grid(row = 11 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_gromar).grid(row = 12 , column = 0)

#same commentting as above
def operate_margin_funt():
    def calc_opermar():
        try:
            ope_mar = float(ope_inc.get())/float(sales.get())
            ope_mar_round = "{:.2f}".format(ope_mar)
            labelly = Label(tab1, text="Your operating margin: " + str(ope_mar_round) + "%" , bg='yellow').grid(row = 21 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row = 19 , column = 0)
            
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row = 15 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="OM - Enter operating income: ").grid(row = 15 , column = 0)
    ope_inc = Entry(tab1 , width=30 , borderwidth = 5)
    ope_inc.grid(row = 16 , column = 0)

    tabb2 = Label(tab1, text="OM - Enter sales here: ").grid(row = 17 , column = 0)
    sales = Entry(tab1 , width=30 , borderwidth = 5)
    sales.grid(row = 18 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_opermar).grid(row = 19 , column = 0)

#same commentting as above
def net_profit_funct():
    def calc_netmar():
        try:
            net_mar = float(net_inc.get())/float(sales.get())
            net_mar_round = "{:.2f}".format(net_mar)
            labelly = Label(tab1, text="Your net profit margin: " + str(net_mar_round) + "%"  ,bg='yellow').grid(row = 28 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row = 26 , column = 0)
            
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row = 22 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="NPM - Enter net income here: ").grid(row = 22 , column = 0)
    net_inc = Entry(tab1 , width=30 , borderwidth = 5)
    net_inc.grid(row = 23 , column = 0)

    tabb2 = Label(tab1, text="NPM - Enter sales here: ").grid(row = 24 , column = 0)
    sales = Entry(tab1 , width=30 , borderwidth = 5)
    sales.grid(row = 25 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_netmar).grid(row = 26 , column = 0)


#This checks which boxes in the checkbox menu have been checked
#If they have been checked they're represented as on (1). If they aren't marked then they're shown as off (0)
#This program ignores any options that are off/havent been checked
#If the box is on (1) it will call the function (and therefore calculation) assosiated to what that checkbox represents i.e gross margin
#If no boxes were checked then the user gets an error message telling them to choose at least one option
def Check_it_1(GM_opt , OM_opt , NPM_opt, bep):
    #The structure of these if statements basically check all the following combinations:
    #Have these been checked? (GM and OM), (GM and NPM) , (GM, OM and NPM) , (OM and NPM) , all of them on their own?
    #if the first, second or third boxes were checked
    if GM_opt.get() == 1:
        #rewriting the continue button from before but changing its state to disabled so the program doesn't constantly call a function that is no longer needed
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        gross_margin_funct() # GM calculations run first
        if OM_opt.get() == 1:
            operate_margin_funt() # OM calculations run second if ticked
        if NPM_opt.get() == 1:
            net_profit_funct() # NPM operations run last if ticked

    #if the second and third boxes were checked
    elif OM_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        operate_margin_funt() # calculations for operating margin run first
        if NPM_opt.get() == 1:
            net_profit_funct() # net profit margin operation calculations run second if ticked

    #if only the third box was checked     
    elif NPM_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        net_profit_funct() # only calculations for net profit are checked
        
     #if no boxes were checked
    else:
        labelly = Label(tab1, text="You didn't enter an option, please enter one below ", bg = "red").grid(row=3 , column = 0)
        #this will continue to show until at least one box as been checked


#The commenting here is the exact same as type 1
def current_ratio_funct():
    def calc_currat():
        try:
            cur_rat = float(cur_ass.get())/float(cur_liab.get())
            cur_rat_round = "{:.2f}".format(cur_rat)
            labelly = Label(tab1, text="Your current ratio: " + str(cur_rat_round) , bg='yellow').grid(row=14 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=12 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=8 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="CUR - Enter current assets here: ").grid(row=8 , column = 0)
    cur_ass = Entry(tab1 , width=30 , borderwidth = 5)
    cur_ass.grid(row=9 , column = 0)

    tabb2 = Label(tab1, text="CUR - Enter current liabilities here: ").grid(row=10 , column = 0)
    cur_liab = Entry(tab1 , width=30 , borderwidth = 5)
    cur_liab.grid(row=11 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_currat).grid(row=12 , column = 0)

#The commenting here is the exact same as type 1
def quick_ratio_funt():
    def calc_quirat():
        try:
            qui_rat = (float(cur_ass.get()) - float(invet.get()))/float(cur_liab.get())
            qui_rat_round = "{:.2f}".format(qui_rat)
            labelly = Label(tab1, text="Your quick ratio: " + str(qui_rat_round) ,bg='yellow').grid(row=23 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=21 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=15 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="QR - Enter current assets here: ").grid(row=15 , column = 0)
    cur_ass = Entry(tab1 , width=30 , borderwidth = 5)
    cur_ass.grid(row=16 , column = 0)

    tabb2 = Label(tab1, text="QR - Enter current liabilities here: ").grid(row=17 , column = 0)
    cur_liab = Entry(tab1 , width=30 , borderwidth = 5)
    cur_liab.grid(row=18 , column = 0)

    tabb3 = Label(tab1, text="QR - Enter inventory here: ").grid(row=19 , column = 0)
    invet = Entry(tab1 , width=30 , borderwidth = 5)
    invet.grid(row=20 , column = 0)
    conti = Button(tab1 , text="Continue" , command=calc_quirat).grid(row=21 , column = 0)

#The commenting here is the exact same as type 1
def cash_ratio_funct():
    def calc_casrat():
        try:
            cas_rat = float(cash.get())/float(cur_liab.get())
            cas_rat_round = "{:.2f}".format(cas_rat)
            labelly = Label(tab1, text="Your cash ratio: " + str(cas_rat_round)  ,bg='yellow').grid(row=30 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=28 , column = 0)

        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=24 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="CashR - Enter cash here: ").grid(row=24 , column = 0)
    cash = Entry(tab1 , width=30 , borderwidth = 5)
    cash.grid(row=25 , column = 0)

    tabb2 = Label(tab1, text="CashR - Enter current liabilities here: ").grid(row=26 , column = 0)
    cur_liab = Entry(tab1 , width=30 , borderwidth = 5)
    cur_liab.grid(row=27 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_casrat).grid(row=28 , column = 0)

#The commenting here is the exact same as type 1
def Check_it_2(CR_opt , QR_opt , CAR_opt, bep):
    if CR_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        current_ratio_funct()
        if QR_opt.get() == 1:
            quick_ratio_funt()
        if CAR_opt.get() == 1:
            cash_ratio_funct()
            
    elif QR_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        quick_ratio_funt()
        if CAR_opt.get() == 1:
            cash_ratio_funct()
            
    elif CAR_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=7 , column=0)
        cash_ratio_funct()
        
            
    else:
        labelly = Label(tab1, text="You didn't enter an option, please enter one below", bg = "red").grid(row=3 , column = 0)


#The commenting here is the exact same as type 1
def debt_equity_funct():
    def calc_debteqt():
        try:
            debteqt = float(Tot_debt.get())/float(Tot_eq.get())
            debteqt_round = "{:.2f}".format(debteqt)
            labelly = Label(tab1, text="Your debt-to-equity is: " + str(debteqt_round) , bg='yellow').grid(row=13 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=11 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=7 , column = 1, rowspan = 3)
        #row span means how many rows this text will fill so the rows aren't expanded to fit a bunch of text into one row
    tabb1 = Label(tab1, text="DTE - Enter total debt here: ").grid(row=7 , column = 0)
    Tot_debt = Entry(tab1 , width=30 , borderwidth = 5)
    Tot_debt.grid(row=8 , column = 0)

    tabb2 = Label(tab1, text="DTE - Enter total equity here: ").grid(row=9 , column = 0)
    Tot_eq = Entry(tab1 , width=30 , borderwidth = 5)
    Tot_eq.grid(row=10 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_debteqt).grid(row=11 , column = 0)

#The commenting here is the exact same as type 1
def debt_capital_funt():
    def calc_debtcap():
        try:
            debtcap = float(Tot_debt.get())/(float(Tot_eq.get()) + int(Tot_debt.get()))
            detbcap_round = "{:.2f}".format(debtcap)
            labelly = Label(tab1, text="Your debt-to-capital is: " + str(detbcap_round), bg='yellow').grid(row=21 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=19 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=14 , column = 1, rowspan = 3)

    tabb1 = Label(tab1, text="DTC - Enter total debt here: ").grid(row=14 , column = 0)
    Tot_debt = Entry(tab1 , width=30 , borderwidth = 5)
    Tot_debt.grid(row=15 , column = 0)

    tabb2 = Label(tab1, text="DTC - Enter total equity here: ").grid(row=16 , column = 0)
    Tot_eq = Entry(tab1 , width=30 , borderwidth = 5)
    Tot_eq.grid(row=18 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_debtcap).grid(row=19 , column = 0)


#The commenting here is the exact same as type 1
def Check_it_3(DTE_opt , DTC_opt, bep):
    #if both first and second box was choses
    if DTE_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=6 , column=0)
        debt_equity_funct()
        if DTC_opt.get() == 1:
            debt_capital_funt()

    #If only the second box was chosen
    elif DTC_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=6 , column=0)
        debt_capital_funt()

            
    else:
        labelly = Label(tab1, text="You didn't enter an option, please enter one below: ", bg = "red").grid(row=3 , column = 0)
        
#The commenting here is the exact same as type 1
def return_equity_funct():
    def calc_reteqt():
        try:
            reteqt = float(net_inc.get())/float(Tot_ass.get())
            reteqt_round = "{:.2f}".format(reteqt)
            labelly = Label(tab1, text="Your return-on-equity is: " + str(reteqt_round), bg='yellow').grid(row=13 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=11 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=7 , column = 1, rowspan=3)

    tabb1 = Label(tab1, text="ROE - Enter net income here: ").grid(row=7 , column = 0)
    net_inc = Entry(tab1 , width=30 , borderwidth = 5)
    net_inc.grid(row=8 , column = 0)

    tabb2 = Label(tab1, text="ROE - Enter total assets here: ").grid(row=9 , column = 0)
    Tot_ass = Entry(tab1 , width=30 , borderwidth = 5)
    Tot_ass.grid(row=10 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_reteqt).grid(row=11 , column = 0)

#The commenting here is the exact same as type 1
def return_assets_funct(): 
    def calc_retass():
        try:
            retass = float(net_inc.get())/float(BVOE.get())
            retass_round = "{:.2f}".format(retass)
            labelly = Label(tab1, text="Your return-on-assets is: " + str(retass_round) ,  bg='yellow').grid(row=20 , column = 0)
            Button(tab1 , text="Continue" , state=DISABLED).grid(row=18 , column = 0)
        except ValueError:
            error_label = Label(tab1, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=14 , column = 1 , rowspan=3)

    tabb1 = Label(tab1, text="ROA - Enter Net income here: ").grid(row=14 , column = 0)
    net_inc = Entry(tab1 , width=30 , borderwidth = 5)
    net_inc.grid(row=15 , column = 0)

    tabb2 = Label(tab1, text="ROA - Enter book value of equity here: ").grid(row=16 , column = 0)
    BVOE = Entry(tab1 , width=30 , borderwidth = 5)
    BVOE.grid(row=17 , column = 0)

    conti = Button(tab1 , text="Continue" , command=calc_retass).grid(row=18 , column = 0)

#The commenting here is the exact same as type 1
def Check_it_4(ROE_opt , ROA_opt, bep):
    if ROE_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=6 , column=0)
        return_equity_funct()
        if ROA_opt.get() == 1:
            return_assets_funct()
    elif ROA_opt.get() == 1:
        Button(tab1, text='Continue', state=DISABLED).grid(row=6 , column=0)
        return_assets_funct()
            
    else:
        labelly = Label(tab1, text="You didn't enter an option, please enter one below ", bg = "red").grid(row=3 , column = 0)


# This is the checkbox menu
# Once the user presses continue, the results of the menu are passed through to the next function
# This determines which calculations need to be done
# IntVar detects if the box has been checked or not
def tp_1():
    bep = Label(tab1, text="Choose a profitability ratio to calculate:").grid(row=3 , column=0)

    GM_opt = IntVar()
    Gro_mar = Checkbutton(tab1, text="Gross Margin", variable=GM_opt).grid(row=4 , column=0)
    
    OM_opt = IntVar()
    Oper_mar = Checkbutton(tab1, text="Operating Margin", variable=OM_opt).grid(row=5 , column=0)

    NPM_opt = IntVar()
    net_mar = Checkbutton(tab1, text="Net Profit Margin", variable=NPM_opt).grid(row=6 , column=0)

    #once the user makes their selection, the program will activate the check it function to see which boxes were ticked
    Button(tab1, text='Continue', command=lambda: Check_it_1(GM_opt , OM_opt , NPM_opt , bep)).grid(row=7 , column=0)

#The commenting here is the exact same as above
def tp_2():
    bep = Label(tab1, text="Choose a profitability ratio to calculate:").grid(row=3 , column=0)

    CR_opt = IntVar()
    Curr_rat = Checkbutton(tab1, text="Current Ratio", variable=CR_opt).grid(row=4 , column=0)
    
    QR_opt = IntVar()
    quick_rat = Checkbutton(tab1, text="Quick Ratio", variable=QR_opt).grid(row=5 , column=0)

    CAR_opt = IntVar()
    cas_rat = Checkbutton(tab1, text="Cash Ratio", variable=CAR_opt).grid(row=6 , column=0)
    
    Button(tab1, text='Continue', command=lambda: Check_it_2(CR_opt , QR_opt , CAR_opt , bep)).grid(row=7 , column=0)

    
#The commenting here is the exact same as above
def tp_3():
    bep = Label(tab1, text="Choose a profitability ratio to calculate:").grid(row=3 , column=0)

    DTE_opt = IntVar()
    debt_eq = Checkbutton(tab1, text="Debt-to-equity", variable=DTE_opt).grid(row=4 , column=0)
    
    DTC_opt = IntVar()
    debt_capt = Checkbutton(tab1, text="Debt-to-capital", variable=DTC_opt).grid(row=5 , column=0)
    
    Button(tab1, text='Continue', command=lambda: Check_it_3(DTE_opt , DTC_opt, bep)).grid(row=6 , column=0)


#The commenting here is the exact same as above  
def tp_4():
    bep = Label(tab1, text="Choose a profitability ratio to calculate:").grid(row=3, column=0)

    ROE_opt = IntVar()
    retu_eq = Checkbutton(tab1, text="Return-on-equity", variable=ROE_opt).grid(row=4 , column=0)
    
    ROA_opt = IntVar()
    retu_as = Checkbutton(tab1, text="Return-on-assets", variable=ROA_opt).grid(row=5 , column=0)
    
    Button(tab1, text='Continue', command=lambda: Check_it_4(ROE_opt , ROA_opt , bep)).grid(row=6 , column=0)


def show(clicked, button):
    #once the user has chosen a type, they can't go back to avoid functions looping over eachother
    #therefore I will redraw a new button over the old one but this will be disabled
    button = Button(tab1, text="Continue", state=DISABLED).grid(row=1 , column=0)
    #tell the user what their choice
    myLabel = Label(tab1, text="Your choice is: " + clicked.get()).grid(row=2 , column=0)
    #whichever option was chosen is taken and stored into choice
    Choice = clicked.get()
    #according to whichever choice the user made, that type of ratio function is called upon
    if Choice == "Type 1: Profitablity ratios":
        tp_1()
    elif Choice == "Type 2: Liquidity ratios":
        tp_2()
    elif Choice == "Type 3: Leverage ratios":
        tp_3()
    elif Choice == "Type 4: Operating ratios":
        tp_4()
  

#This is where tab 1 actually starts
#User has a drop down box with all 4 types of ratios and can choose which one of the 4 to progress with
def start():
    OPTIONS = [
    "Type 1: Profitablity ratios",
    "Type 2: Liquidity ratios",
    "Type 3: Leverage ratios",
    "Type 4: Operating ratios"]

    # lets the user click the drop box in the first tab
    clicked = StringVar(tab1)
    # when you load the screen the first option in the list is the default option. right now its Type 1
    clicked.set(OPTIONS[0])
    #puts all our preferences into a single variable and draws it up in the form of a drop box
    w = OptionMenu(tab1, clicked, *OPTIONS).grid(row=0 , column=0)

    button = Button(tab1, text="Continue", command=lambda: show(clicked, button)).grid(row=1 , column=0)
    
######################################TAB 2 STARTS HERE

#once the user has chosen which value they want to calculate and entered the nessasary information calc_stuff() is called
# Depending on whichever calculation is selected, like with tab 1, exception handling is used to make sure the right dataype is inputted
#After the program has reached an answer the answer is reformatted so it will only give upto 2 d.p.
#The output is highlighted in yellow like the output in task 1
def start_2(clickeri):
    def calc_stuff(clickeri):
        if clickeri.get() == "Present value":
            try:
                #assuming that the user is entering as a percentage so must convert to a decimal annual interest rate
                dec_of_an_int = float(an_int.get())/100
                #x is the denominator, just making the steps of calculation clearer
                #the first paramenter of pow is the base and the second (number of years) is the exponent to get us the power of
                x = pow((1+dec_of_an_int) ,float(n_yrs.get()))
                pv = float(efv.get())/float(x)
                pv_round = "{:.2f}".format(pv)
                labelly = Label(tab2, text="Your present value: " + str(pv_round) , bg = 'yellow').grid(row=13 , column = 0)
                Button(tab2 , text="Continue" , state=DISABLED).grid(row=11 , column = 0)
            except ValueError:
                error_label = Label(tab2, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=12 , column = 0)
            
        elif clickeri.get() == "Future value":
            try:
                dec_of_an_int = float(an_int.get()) / 100
                x = pow((1 + dec_of_an_int), float(n_yrs.get()))
                #like earlier but x is a multiplier here
                fv = float(am_inv.get()) * x
                fv_round = "{:.2f}".format(fv)
                labelly = Label(tab2, text="Your future value: " + str(fv_round) , bg = 'yellow').grid(row=13 , column = 0)
                Button(tab2 , text="Continue" , state=DISABLED).grid(row=11 , column = 0)
            except ValueError:
                error_label = Label(tab2, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=12, column = 0)
            
    #Both present and future value need the same information
    #irregardless of which option is chosen the user can entre the annual interest rate and period of time
    #if they've chosen FV, they'll be prompted to enter amount invested
    # if PV then they enter their estimated FV
    Button(tab2, text="Continue", state=DISABLED).grid(row=2, column = 0)
    tabb1 = Label(tab2, text="IF FUTURE VALUE, enter amount invested here: ").grid(row=3 , column = 0)
    am_inv = Entry(tab2 , width=30 , borderwidth = 5)
    am_inv.grid(row=4 , column = 0)

    #variables called tab because
    tabb11 = Label(tab2, text="IF PRESENT VALUE, enter your estimated future value: ").grid(row=5, column=0)
    efv = Entry(tab2, width=30, borderwidth=5)
    efv.grid(row=6, column=0)
    
    tabb2 = Label(tab2, text="Enter annual interest rate here (as a %): ").grid(row=7 , column = 0)
    an_int = Entry(tab2 , width=30 , borderwidth = 5)
    an_int.grid(row=8 , column = 0)

    tabb3 = Label(tab2, text="Enter number of years here: ").grid(row=9 , column = 0)
    n_yrs = Entry(tab2 , width=30 , borderwidth = 5)  #the borderwidth just makes the input box more defined and pretty
    n_yrs.grid(row=10 , column = 0,columnspan = 2)
    #the function calc stuff will be called when the continue button is pressed. This will decide if it needs to run the code for PV or FV
    conti = Button(tab2, text="Continue", command=lambda: calc_stuff(clickeri)).grid(row=11, column=0)



#This is where tab 2 starts, same as tab 1 the user can choose between future value or present value
def tell():
    #I've decided to use a dropbox so the user can choose only the FV or PV
    labelicity = Label(tab2 , text= "Choose a time value of money: ").grid(row=0 , column = 0)
    OPTIONS = ["Present value" , "Future value"]
    clickeri = StringVar(tab2)
    clickeri.set(OPTIONS[0]) # the default drop box option is the first in the list which is this case is present value
    w = OptionMenu(tab2, clickeri, *OPTIONS).grid(row=1 , column = 0)
    #By pressing continue, it activates the start_2 which identifies which calculation the user has selected to perform
    # it calls the function according to the selection
    button = Button(tab2, text="Continue", command=lambda: start_2(clickeri)).grid(row=2, column = 0)


######################################### TAB 3 STARTS HERE

#depending on what checkbozes were checked will these functions activate
def NPV_funct(ANS_NPV):
    ANS_NPV_round = "{:.2f}".format(ANS_NPV)
    Label(tab3 , text="Your net present value is: " + str(ANS_NPV_round) , bg="yellow").grid(row=22, column = 0, columnspan = 3)

def IRR_funct(ANS_IRR):
    ANS_IRR_round = "{:.2f}".format(ANS_IRR)
    Label(tab3 , text="Your internal rate of return is: " + str(ANS_IRR_round) + "%", bg="yellow").grid(row=23, column = 0, columnspan = 3)
    

def PP_funct(ANS_PP):
    ANS_PP_round = "{:.2f}".format(ANS_PP)
    Label(tab3 , text="Your payback period is: " + str(ANS_PP_round) + "years" , bg="yellow").grid(row=24, column = 0, columnspan = 3)

def calc_and_choice(PP_opt ,IRR_opt, NPV_opt, ini_inv_p, py_1_i, py_2_i, py_3_i, py_4_i, py_5_i, py_1_o, py_2_o, py_3_o, py_4_o, py_5_o, dis_rat_p):
    try:
        #getting everything entered and storing it into a new variable as a float rather than its default string
        Y1I = float(py_1_i.get())
        Y2I = float(py_2_i.get())
        Y3I = float(py_3_i.get())
        Y4I = float(py_4_i.get())
        Y5I = float(py_5_i.get())

        Y1O = float(py_1_o.get())
        Y2O = float(py_2_o.get())
        Y3O = float(py_3_o.get())
        Y4O = float(py_4_o.get())
        Y5O = float(py_5_o.get())

        DR_full = float(dis_rat_p.get())
        DR = DR_full/100
        II = float(ini_inv_p.get())

        #For simplicity sake  (so i don't have to continously pass variables) i'm going to calculate all options
        #then once the user has selected a calculation it will only output THAT answer

        #calculation net present value
        #IMplementing the equation
        ANS_NPV = (-II/pow((1+DR) , 0)) + ((Y1I-Y1O)/pow((1+DR) , 1)) + ((Y2I-Y2O)/pow((1+DR) , 2)) + ((Y3I-Y3O)/pow((1+DR) , 3)) + ((Y4I-Y4O)/pow((1+DR) , 4)) + ((Y5I-Y5O)/pow((1+DR) , 5))
    
        #calculation internal rate of return
        #i'm using the inbuilt IRR function that Numpy-financial has
        ANS_IRR = (npf.irr([-II, (Y1I - Y1O), (Y2I - Y2O), (Y3I - Y3O), (Y4I - Y4O), (Y5I - Y5O)]))
        ANS_IRR = ANS_IRR* 100
        
        #calculation payback period
        #calculating cash flow (inflow - outflow)
        a = Y1I-Y1O
        b = Y2I-Y2O
        c = Y3I-Y3O
        d = Y4I-Y4O
        e = Y5I-Y5O

        y1t = a #all money earnt by end of yr 1
        y2t = a + b #all money earnt by end of yr 2
        y3t = a + b + c #all money earnt by end of yr 3
        y4t = a + b + c + d #all money earnt by end of yr 4
        y5t = a + b + c + d + e #all money earnt by end of yr 5

        #if everything earnt by yr 1 is greater than the initial investment
        #this means they have earnt back their investment in under a year
        #Implementing the equation
        if y1t>II:
            PAL = II-0
            ANS_PP = 0+(PAL/a)
        elif y2t>II:
            PAL = II-y1t
            ANS_PP = 1+(PAL/b)
        elif y3t>II:
            PAL = II-y2t
            ANS_PP = 2+(PAL/c)
        elif y4t>II:
            PAL = II-y3t
            ANS_PP = 3+(PAL/d)
        elif y5t>II:
            PAL = II-y3t
            ANS_PP = 4+(PAL/e)
        else: # this means that despite the inflow from the past 5 years, the investment value is still greater
            ANS_PP = "You will not be able to pay back your investment in the next 5 years"


        #This identifies which checkboxes have been selected
        if NPV_opt.get() == 1:
            Button(tab3, text='Continue', state=DISABLED).grid(row = 19, column = 1)
            NPV_funct(ANS_NPV)
            if IRR_opt.get() == 1:
                IRR_funct(ANS_IRR)
            if PP_opt.get() == 1:
                PP_funct(ANS_PP)

        elif IRR_opt.get() == 1:
            Button(tab3, text='Continue', state=DISABLED).grid(row = 19, column = 1)
            IRR_funct(ANS_IRR)
            if PP_opt.get() == 1:
                PP_funct(ANS_PP)

        elif PP_opt.get() == 1:
            Button(tab3, text='Continue', state=DISABLED).grid(row = 19, column = 1)
            PP_funct(ANS_PP)
            
        else:
            labelly = Label(tab3, text="You didn't enter an option, please enter one above ", bg = "red").grid(row=21 , column = 0, columnspan = 3)
    except ValueError:
        labelly = Label(tab3, text="You didn't enter the right values. \n\
Try again with the right data type \n\
Press continue once you've entered a number", bg = "red").grid(row=20 , column = 0, columnspan = 3)

def start_3():
    #Creating a label to put next to the entry box so the user knows what the entry box is looking for
    myLabelA = Label(tab3, text="Cash inflow").grid(row=6, column=1)
    myLabelB = Label(tab3, text="Cash outflow").grid(row=6, column=2)
    y_1 = Label(tab3, text="Year 1").grid(row=7, column=0)
    y_2 = Label(tab3, text="Year 2").grid(row=8, column=0)
    y_3 = Label(tab3, text="Year 3").grid(row=9, column=0)
    y_4 = Label(tab3, text="Year 4").grid(row=10, column=0)
    y_5 = Label(tab3, text="Year 5").grid(row=11, column=0)


    #creating the entry box for everything the equations will need to calculate the final values
    py_1_i = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_1_i.grid(row=7 , column=1)

    py_2_i = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_2_i.grid(row=8 , column=1)

    py_3_i = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_3_i.grid(row=9 , column=1)

    py_4_i = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_4_i.grid(row=10 , column=1)

    py_5_i = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_5_i.grid(row=11 , column=1)


    py_1_o = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_1_o.grid(row=7 , column=2)

    py_2_o = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_2_o.grid(row=8 , column=2)

    py_3_o = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_3_o.grid(row=9 , column=2)

    py_4_o = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_4_o.grid(row=10 , column=2)

    py_5_o = Entry(tab3 , width = 10 ,borderwidth = 5)
    py_5_o.grid(row=11 , column=2)

    gap = Label(tab3 , text=" ").grid(row=12 , column=0)

    myLabel2 = Label(tab3 , text="Discount rate: ").grid(row=13 , column=0)
    dis_rat_p = Entry(tab3 , width = 20 , borderwidth = 5)
    dis_rat_p.grid(row=13, column=1 , columnspan=3)

    myLabel = Label(tab3 , text="Initial investment: ").grid(row=14, column=0)
    ini_inv_p = Entry(tab3 , width = 20 , borderwidth = 5)
    ini_inv_p.grid(row=14, column=1, columnspan=2)

    beppy = Label(tab3, text="Choose a calculaton:")
    beppy.grid(row = 15, column = 0, columnspan = 3)



    #The user will recieve the user entry form and the checkbox option (for whichever calculation they need) at the same time
    NPV_opt = IntVar()
    NPV_BUT = Checkbutton(tab3, text="Net present value", variable=NPV_opt).grid(row=16, column=0, columnspan=3)

    IRR_opt = IntVar()
    IRR_BUT = Checkbutton(tab3, text="Internal rate of return", variable=IRR_opt).grid(row = 17, column = 0, columnspan = 3)

    PP_opt = IntVar()
    PP_BUT = Checkbutton(tab3, text="Payback period", variable=PP_opt).grid(row = 18, column = 0, columnspan = 3)

    #In the next function 'continue' will lead to, I'm passing every piece of data the user has entered to be used in a later stage)
    Button(tab3, text='Continue', command=lambda: calc_and_choice(PP_opt ,IRR_opt, NPV_opt, ini_inv_p, py_1_i, py_2_i, py_3_i, py_4_i, py_5_i, py_1_o, py_2_o, py_3_o, py_4_o, py_5_o, dis_rat_p)).grid(row = 19, column = 1)
    


##################THIS CALLS EACH OF THE TABS
start_3() # TAB 3
tell() # TAB 2
start() # TAB 1
refresh_tab() # Refresh tab (aka tab 4)

#This is required to see when each event is happening
master.mainloop()
