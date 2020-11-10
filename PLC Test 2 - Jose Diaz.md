## PLC Test 2 - Jose Diaz


1. dsad
2. (9 points) Write three functions in C or C++: one that declares a large array statically, one that declares the same large array on the stack, and one that creates the same large array from the heap. Call each of the subprograms a large number of times (at least 100,000) and output the time  required by each. Explain the results.
	
	- For this program I wrote mine in C. This question was actually not too hard and I enjoyed it because it had been a while since I programmed in C. 
	- Anyways, for my program I created arrays that were of length/size 10000 and then I ran each function for 10,000,000. AKA 10 million times
	- After waiting for the execution the reults were the following:
	- the stack function was the quickest taking only .020545 seconds
	- Second quickest was the static function which took .021356 seconds
	- And finally the slowest by far was the heap function which took 15.688600 seconds
	- I belive that the reason the stack is the fastest is because pushing on to the stack is incredibly easy. It probably happens instantly. While when we are doing the heap we have to allocate space in memory and then deal with pointers and anytime we have to go to memory we are slowed down significantly.
	- The stack is better for anything short term that only needs to be there when the function is alive then we can use the stack.
	- But if we are dealing with big arrays or structs that can change in size then we should use the heap.
	- I have included the output in a txt file as well
	- And here is the source code
	- jose_question2.c
	
	```
	// question2_jose.c
		
		#include <stdio.h>
		#include <stdlib.h>
		#include <time.h>
		
		int staticArr();
		int stackArr();
		int heapArr();
		
		int main() {
		
		  // Now here I will try to get the amount of time that each function takes.
		  // I will run it 10000000 times bc i don't want to blow up my computer lol
		
		
		  // the code for finding out how long it takes to run is from
		  // geeks for geeks
		  // https://www.geeksforgeeks.org/how-to-measure-time-taken-by-a-program-in-c/
		
		   printf("Hello, World! \n");
		
		   clock_t first;
		   first = clock();
		
		   for(int i = 0; i < 10000000; i++){
		     staticArr();
		   }
		
		   first = clock() - first;
		   double firstTime = ((double)first) / CLOCKS_PER_SEC;
		   printf("staticArr() took %f seconds to execute \n", firstTime);
		
		   clock_t second;
		   second = clock();
		
		   for(int i = 0; i < 10000000; i++){
		     stackArr();
		   }
		
		   second = clock() - second;
		   double secondTime = ((double)second) / CLOCKS_PER_SEC;
		   printf("stackArr() took %f seconds to execute \n", secondTime);
		
		   clock_t third;
		   third = clock();
		
		   for(int i = 0; i < 10000000; i++){
		     heapArr();
		   }
		
		   third = clock() - third;
		   double thirdTime = ((double)third) / CLOCKS_PER_SEC;
		   printf("heapArr() took %f seconds to execute \n", thirdTime);
		
		   printf("---- Jose Diaz ----\n");
		   return 0;
		}
		
		int staticArr() {
		
		  // not sure if this is correct. have to declare 'statically' and this is the static
		  // keyword sooo. But I read that static means that the variable can only be accessed
		  // from the file that created it but still shaky on this
		  // i read the info from here: http://www.mathcs.emory.edu/~cheung/Courses/255/Syllabus/1-C-intro/scope-global.html
		
		   static int balance[10000];
		
		   // for(int i = 0; i < 1000; i++){
		   //   balance[i] = i;
		   //   //printf("%d", balance[i]);
		   // }
		
		   return 0;
		}
		
		int stackArr() {
		
		  // this one is also weird bc whenever you make a variable in a function it goes on the stack
		  // sooooo
		  // this is it???
		
		  int stacked[10000];
		
		  return 0;
		}
		
		int heapArr(){
		
		  // Inspiration for this part came from:
		  // https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html
		  // this part showed that to do it in a heap you had to use
		  // the malloc function
		
		  int *heaped = malloc(10000 * sizeof(int));
	
	  return 0;
	}

	```
	
	- output is also here:
	
	```
	Hello, World! 
	staticArr() took 0.021356 seconds to execute 
	stackArr() took 0.020545 seconds to execute 
	heapArr() took 15.688600 seconds to execute 
	---- Jose Diaz ----

	```
3. asd
4. adads
5. fsaf
6. fasfa
7. fafsfa
8. (10 points) Perl allows both static and a kind of dynamic scoping. Write a Perl program that uses both and clearly shows the difference in effect of the two. Explain clearly the difference between the dynamic scoping described in this chapter and that implemented in Perl.

	- In my program you can see that when we dynamically scope we are grabbing the value from the closest place the variable was declared.
	- When we statically scope we are actually grabbing the value from the parent function
	- In my program I also explain in the comments
	
	```
	
	# so from geeks for geeks in order to get dynamically scoped varible we just use keywords
	# my keyword defines a statically scoped local variable
	# and local defines dynamically scoped local variable
	#
	# link: https://www.geeksforgeeks.org/static-and-dynamic-scoping/
	
	print "Hello World!\n";
	$mainVar = 100;
	$mainVar2 = 100;
	
	sub showVar1
	{
	  return $mainVar;
	}
	sub dynamic
	{
	  # use local which gives us dynamically scoped var
	  # here since we are dynamic we are grabbing from the closest place it was declared
	  local $mainVar = 1;
	  return showVar1();
	}
	
	sub showVar2
	{
	    return $mainVar2;
	}
	sub static
	{
	    # use my which gives us the statically scoped var
	    # here instead of grabbing what is closest to us we are grabbing the value from the 'parent' function
	    my $mainVar2 = 1;
	    return showVar2();
	}
	
	print dynamic()." ------ DYNAMIC\n";
	print static()." ------ STATIC\n";
	print "---- Jose Diaz ----";

	```
	
	- Output is also in txt file and here
	
	```
	Hello World!
	1 ------ DYNAMIC
	100 ------ STATIC
	---- Jose Diaz ----

	```
