print("==welcome==")
def calculate(*args,**kwargs):
    """This act as fuction decalartion of rthe argument will be used by using arsterics """
    for x in args:
        if not isinstance(x,(int,float)):
            raise ValueError("Invalid input")
    if not args:
          raise ValueError("No Number")
    Operation=["Add","Multiply"]
    get_operation=[y for y in Operation if kwargs.get(y)]
    if len(get_operation) !=1:
         raise ValueError
    Operation=get_operation[0]
    return process(Operation, *args)
def process(Operation, *args):
      """This help to determine the fuction of each opereation  by calculation and how fuction return"""
      if Operation=="Add":
            return sum(args)
      if Operation=="Multiply":
         result=1
         for number in args:
            result*=number
         return result
    
def main():
    """This help us to make  fuction calling"""
    try:
        print("Choose Operation:\n1.Add\n2.Multiply")
        choice=input("Enter your choice : ").strip()
        Numbers=input("Enter numbers separated by space : ").split()
        input_Number=[float(x) for x in Numbers]
        if choice=="1":
          result = calculate(*input_Number, Add=True)
        elif choice=="2":
          result = calculate(*input_Number, Multiply=True)
        else:
            raise ValueError("Invalid option")
        print(f"Result : {result}")
    
    except Exception as e:
        print(f"Error : {e}")
if __name__=="__main__":
    main()
          

      