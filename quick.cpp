#include <iostream>
using namespace std;

// Quick Sort için partition fonksiyonu
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Pivot olarak son elemanı alıyoruz
    int i = low - 1;        // Küçük elemanların indexi

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Quick Sort fonksiyonu
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Diziyi yazdırmak için yardımcı fonksiyon
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Main
int main() {
    int arr[] = {64, 32, 76, 98, 54, 54, 33, 88, 66, 12, 37};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    cout << "Sorted array:   ";
    printArray(arr, n);

    return 0;
}
