#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int find_min(int i, int calculated, int total, vector<int> n) {
  if (i == 0) 
    return abs((total - calculated) - calculated);
  return min(find_min(i - 1, calculated, total, n), find_min(i - 1, calculated + n[i - 1], total, n));
}

int main() {
  int x, soma = 0;
  vector<int> n;
  cin >> x;
  while (cin >> x) {
    n.push_back(x);
    soma += x;
  }
  x = find_min(n.size(), 0, soma, n);
  cout << x;
  return 0;
}
