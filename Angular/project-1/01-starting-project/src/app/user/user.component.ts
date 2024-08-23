import { Component } from '@angular/core';
import { DUMMY_USERS as userList} from '../dummy-users';

const randomIndex = Math.trunc( Math.random() * userList.length )

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [],
  templateUrl: './user.component.html',
  styleUrl: './user.component.css'
})
export class UserComponent {
  selectedUser = userList[randomIndex];

  //Getter che permette di costruire la path dell'avatar
  get avatarPath(){
    return 'assets/users/' + this.selectedUser.avatar
  }

  onSelectUser(){
    const newRandomIndex = Math.floor(Math.random() * userList.length);
    this.selectedUser = userList[newRandomIndex];
  }
}
