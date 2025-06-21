const regex1 = /pattenr/

const regex2 = new RegExp('pattern')

// regex1.test(string) //true or false

// regex1.exec(string) //matched result or null

// [abc] - matches any one of a, b or c

//[^abc] - matches any character except a, b or c

//[a-z] - matches any lowercase letter

// [A-Z] - matches any uppercae letter

// [0-9] - mathces any digit

let regex = /[aeiou]/

console.log(regex.test('ball'))

// . - any character except newline

// \d - any digit (0-9)

// \D - any non digit

// \w - any word character (letters, digits, underscore)

// \W - any non word character

// \s - any whitespace (space, tab, newline)

// \S - any non whitespace

regex = /\d/

console.log(regex.test('abcd'))
// * - 0 or more
// + - 1 or more
// ? - 0 or 1
// {n} - exactly n time
// {n,} - n or more times
// {n,m} - between n and m times
regex = /\d{3}/
console.log(regex.test('abcd12343456456454545'))
// ^ - start of string
// $ - end of string
regex = /Hello$/
console.log(regex.test("test Hello"))