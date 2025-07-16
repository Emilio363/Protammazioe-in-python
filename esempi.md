

### mergerSort

$T(n) = T(n/2) + T(n/2) + O(n) = 2\cdot T(n/2) + O(n)$\
$T(n/2) = T(n/4) + T(n/4) + O(n/2) = 2\cdot T(n/4) + O(n/2)$\
$T(n) = 2\cdot T(n/2) + O(n) = 2\cdot (2\cdot T(n/4) + O(n/2)) + O(n) =$\
$ 4*T(n/4) + 2*O(n/2) + O(n) = 4*T(n/4) + 2*O(n)$

$T(n) = \displaystyle\sum^{\log_2{n}}_{i=1}O(n) = \log_2{n}\cdot O(n) = O(n\cdot \log_2{n})$

### digit_sum_ric
$$
T(n) = O(1) + O(1) + T(n/10)\\
T(n/10) = O(1) + T(n/100)\\
T(n/100) = O(1) + T(n/1000)\\

T(n) = O(1) + O(1) + O(1) + T(n/1000) \\
log_{10}(n) \cdot O(1) = O(log_{10}(n)) $$

### isPrimeRic
$$
T(n, i) = O(1) + T(n, i+1)\\
T(n, i+1) = O(1) + T(n, i+2)\\
T(n, i+2) = O(1) + T(n, i+3)\\
T(n, i) = O(1) + O(1) + O(1) + T(n, i+3)$$

$ i^2 = n \;\;\Rightarrow \;\; i=\sqrt{n}$

$T(n,i) = \displaystyle\sum^{\sqrt{n}}_{i=2}\;O(1) = \sqrt{n}\;\cdot O(1) = O(\sqrt{n})$

