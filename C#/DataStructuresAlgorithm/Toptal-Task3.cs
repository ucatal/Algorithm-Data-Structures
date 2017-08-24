using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructuresAlgorithm
{
    class Task3Test
    {
        static int Task3(int[] A, int D)
        {
            //write your code in C# 6.0 with .NET 4.5 (Mono)

            int N = A.Length;
            if (D > N)
                return 0;
            int position = -1;
            int oldPosition = -1;
            int time = 0;
            int stonesWontSurface = 0;

            while (stonesWontSurface != D)
            {
                oldPosition = position;
                stonesWontSurface = 0;

                for (int i = position + D; i > position; i--)
                {
                    if (i >= A.Length)
                        return time;
                    if (A[i] == -1)
                        stonesWontSurface++;
                    else if (A[i] <= time)
                    {
                        position = i;
                    }
                }

                if (stonesWontSurface == D)
                    return -1;

                if (position == oldPosition)
                {
                    //optimization,no need to increment time one by one
                    int minimumTimeToStoneSurfacing = int.MaxValue;
                    for (int i = position + D; i > position; i--)
                    {
                        if (A[i] < minimumTimeToStoneSurfacing && A[i] > time)
                        {
                            minimumTimeToStoneSurfacing = A[i];
                        }
                    }
                    time = minimumTimeToStoneSurfacing;
                    //time++;
                }
            }
            return time;
        }

    }
}
