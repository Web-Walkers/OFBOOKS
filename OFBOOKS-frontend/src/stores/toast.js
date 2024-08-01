import { defineStore } from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        toastList: [],
        id: 0,
    }),

    actions: {
        deleteToast(itemID) {
            setTimeout(() => {
                this.toastList[itemID].classes += ' translate-x-96 opacity-0 duration-[2000ms]'
            }, this.toastList[itemID].ms - 2000)

            setTimeout(() => {
                this.toastList[itemID].isVisible = false
                if (itemID + 1 == this.id) {
                    this.toastList = []
                    this.id = 0
                }
            }, this.toastList[itemID].ms)
        },

        showToast(itemID) {
            setTimeout(() => {
                this.toastList[itemID].classes = this.toastList[itemID].classes.replace('translate-y-28 opacity-0 duration-800', '')
            }, 10)

            this.deleteToast(itemID)
        },

        addToast(ms, message, category) {
            this.toastList.push({
                ms: parseInt(ms),
                message: message,
                category: category,
                classes: ' translate-y-28 opacity-0 duration-800',
                isVisible: true,
                id: this.id,
            })

            this.showToast(this.id++)
        }
    }
})