namespace PythonLabs
{
    public static class Number
    {
        private const int _number = 5000;

        private static int[] _p = Enumerable.Range(1, _number).ToArray();
        private static int[] _q = Enumerable.Range(1, _number).Select(x => x * 2).ToArray();

        public static double[,] SingleTask()
        {
            double[,] numbers = new double[_number, _number];
            for (int i = 0; i < _number; i++)
            {
                for (int j = 0; j < _number; j++)
                {
                    numbers[i, j] = 1 / (1 + Math.Pow(_q[j] - _p[i], 2));
                }
            }

            return numbers;
        }

        public async static Task<double[,]> ParallelSharedMultiTask()
        {
            int ProcessorCount = Environment.ProcessorCount;
            int count = (int)Math.Ceiling((double)_number / ProcessorCount);

            double[,] numbers = new double[_number, _number];

            var result = Parallel.For(1, ProcessorCount, (i) =>
            {
                int c = count * i;
                if (c < _number)
                    Expression(numbers, count * (i - 1), c);
                else
                    Expression(numbers, count * (i - 1), _number);
            });

            return numbers;
        }

        public async static Task<double[,]> SharedMultiTask()
        {
            int ProcessorCount = Environment.ProcessorCount;
            int count = (int)Math.Ceiling((double)_number / ProcessorCount);
            Task[] tasks = new Task[ProcessorCount];

            double[,] numbers = new double[_number, _number];
            int i;

            for (i = 1; i <= tasks.Length; i++)
            {
                if (count * i < _number)
                    tasks[i - 1] = Task.Factory.StartNew((i) => Expression(numbers, count * ((int)i! - 1), count * (int)i), i);
                else
                    tasks[i - 1] = Task.Factory.StartNew((i) => Expression(numbers, count * ((int)i! - 1), _number), i);

                //Thread.Sleep(1);
            }
            Task.WaitAll(tasks);
            return numbers;
        }

        public static void Expression(double[,] numbers, int start = 0, int end = _number)
        {
            for (int i = start; i < end; i++)
            {
                for (int j = 0; j < _number; j++)
                {
                    numbers[i, j] = 1 / (1 + Math.Pow(_q[j] - _p[i], 2));
                }
            }
        }

        #region <== Old ==>
        //public async static Task<double[,]> MultiTask()
        //{
        //    int ProcessorCount = Environment.ProcessorCount;
        //    int count = (int)Math.Ceiling((double)_number / ProcessorCount);

        //    var numbers = new List<double[,]>();

        //    for (int i = 1; i <= ProcessorCount; i++)
        //    {
        //        var c = count * i;
        //        if (c < 5000)
        //            numbers.Add(await Expression(count * (i - 1), c));
        //        else
        //            numbers.Add(await Expression(count * (i - 1), _number));
        //    }

        //    var expression = await Expression();
        //    return expression;
        //}

        //private static ValueTask<double[,]> Expression(int start = 0, int end = _number)
        //{
        //    double[,] numbers = new double[end - start, _number];
        //    for (int i = start; i < end; i++)
        //    {
        //        for (int j = 0; j < _number; j++)
        //        {
        //            numbers[i, j] = 1 / (1 + Math.Pow(_q[j] - _p[i], 2));
        //        }
        //    }
        //    return new ValueTask<double[,]>(numbers);
        //}

        #endregion
    }
}
