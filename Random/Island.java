class Island
{
    public int[] product(int[] nums)
    {
        int[] running = new int[nums.length];
        running[0] = 1;

        for (int i = 1; i < nums.length; i++)
        {
            running[i] = running[i - 1] * nums[i - 1];
        }

        int runner = 1;
        for (int i = nums.length - 1; i >= 0; i--)
        {
            running[i] *= runner;
            runner *= nums[i];
        }
        return running;
    }
}

