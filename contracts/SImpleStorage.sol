// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {

    // this will get initialized to 0!
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;  // Like a dictionary

    People public person = People({favoriteNumber: 2, name: "Mike"});

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view means it can only read - not write. gas-less
    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }

    // memory will only store during the function call.
    // storage will persist after the function call
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
        // people.push(People(_favoriteNumber, _name)); // this also works
    }
}