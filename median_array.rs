pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (short, long) = if nums1.len() < nums2.len() {
            (nums1, nums2)
        } else {
            (nums2, nums1)
        };
    let (m, n) = (short.len(), long.len());
    let mut l = 0;
    let mut r = m;
    while l <= r {
        let i = l + (r - l) / 2;
        let j = (m + n + 1) / 2 - i;
        let black_left = if i == 0 {
            long[j - 1]
        } else if j == 0 {
            short[i - 1]
        } else {
            long[j - 1].max(short[i - 1])
        };
        let black_right = if i == m {
            long[j]
        } else if j == n {
            short[i]
        } else {
            long[j].min(short[i])
        };
        if black_left <= black_right {
            if (m + n) % 2 == 0 {
                return (black_left + black_right) as f64 / 2.0;
            } else {
                return black_left as f64;
            }
        } else if i > 0 && long[j] < short[i - 1] {
            r = i - 1;
        } else {
            l = i + 1;
        }
    }
    unreachable!()
}
