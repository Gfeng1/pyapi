#!/usr/bin/python3

def main():
            
    dream_cars = [ 'lambo', 'bugatti', 'bentley' ]

    more_likely = [ 'ford', 'toyota', 'honda' ]

    print(dream_cars)
    
    dream_cars.extend(more_likely)

    print(dream_cars)
    print(dream_cars[2])
    print(dream_cars[4])

if __name__ == "__main__":
    main()
                        
