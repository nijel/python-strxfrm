#include <locale.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <wchar.h>
#include <errno.h>

int main(int argc, char** argv) {
    wchar_t *buf;
    size_t len;
    wchar_t string[] = L"zkouška žřščřščřšě";
    wchar_t string2[] = L"zkouska zrscrscrse";
    int i;

    buf = malloc(sizeof(wchar_t) * 400);

    printf("setlocale=%s\n", setlocale(LC_ALL, "en_US.UTF-8"));

    for (i = 0; i < 10000; i++ ) {
        errno = 0;
        printf("wcsxfrm(1)=%zd / %d\n", wcsxfrm(buf, string, 1), errno);
        errno = 0;
        printf("wcsxfrm(40)=%zd / %d \n", wcsxfrm(buf, string, 400), errno);
        printf("buf=%ls\n", buf);
        printf("wcsxfrm(40)=%zd / %d \n", wcsxfrm(buf, string2, 400), errno);
        printf("buf=%ls\n", buf);
    }
}
