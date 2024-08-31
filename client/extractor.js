import users from './MOCK_DATA.json' assert { type: 'json' }

let userArray = []

users.forEach((userObject) => {
    userArray.push(userObject.username)
    return userArray
})




export default userArray