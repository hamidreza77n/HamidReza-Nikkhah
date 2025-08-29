#!/bin/bash
echo "انتخاب حالت اجرا:"
echo "1) توسعه (لوکال پایتون)"
echo "2) پایدار (داکر)"
read -p "عدد مورد نظر را وارد کنید: " choice

if [ "$choice" == "1" ]; then
    ./run_dev.sh
elif [ "$choice" == "2" ]; then
    ./run.sh
else
    echo "❌ گزینه نامعتبر"
fi
