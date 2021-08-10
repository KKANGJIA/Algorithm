<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        function solution(s) {
            const arr = s.split('')
            const pivot = Math.floor(arr.length/2)
            return arr.length % 2 ? arr[pivot] : arr.slice(pivot-1,pivot+1).join('') 
        }
    </script>
</body>
</html>