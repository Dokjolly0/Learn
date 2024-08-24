import { Component } from '@angular/core';
import { DUMMY_USERS as userList } from '../dummy-users';

const randomIndex = Math.floor(Math.random() * 6);
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [],
  templateUrl: './user.component.html',
  styleUrl: './user.component.css',
})
export class UserComponent {
  selectedUser = userList[randomIndex];
  get avatarPath() {
    return `assets/users/${this.selectedUser.avatar}`;
  }
  changeUser() {
    const randomIndex = Math.floor(Math.random() * 6);
    this.selectedUser = userList[randomIndex];
  }
}
