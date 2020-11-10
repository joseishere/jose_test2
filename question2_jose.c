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
