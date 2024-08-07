import { Component } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-text-form',
  templateUrl: './text-form.component.html',
  styleUrls: ['./text-form.component.css']
})
export class TextFormComponent {
  text: string = '';
  key: string = '';
  url: string = '';

  async onSubmit() {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/create', {
        text: this.text,
        key: this.key
      });
      this.url = response.data.url;
    } catch (error) {
      console.error('Error creating snippet:', error);
    }
  }
}