using PythonLabs;
using System.Diagnostics;

Stopwatch stopwatch = new Stopwatch();

Console.WriteLine("Lab 6\nSingle Task\n");

stopwatch.Start();

var singleTask = Number.SingleTask();

stopwatch.Stop();

Console.WriteLine(stopwatch.Elapsed.TotalSeconds + " sec\n");
Console.WriteLine("Shared MultiTask\n");

stopwatch.Restart();
stopwatch.Start();

var sharedMultiTask = await Number.SharedMultiTask();

stopwatch.Stop();

Console.WriteLine(stopwatch.Elapsed.TotalSeconds + " sec\n");
Console.WriteLine("Parallel Shared MultiTask\n");

stopwatch.Restart();
stopwatch.Start();

var parallelSharedMultiTask = await Number.ParallelSharedMultiTask();

stopwatch.Stop();

Console.WriteLine(stopwatch.Elapsed.TotalSeconds + " sec\n");
Console.WriteLine("The end\n");

//stopwatch.Restart();
//stopwatch.Start();

//var multiTask = await Number.MultiTask();

//stopwatch.Stop();

//Console.WriteLine(stopwatch.Elapsed.TotalSeconds + " sec\n");
