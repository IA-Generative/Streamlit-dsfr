<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButtonGroup } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		align?: 'left' | 'center' | 'right'
		inlineLayoutWhen?: 'never' | 'always' | 'small' | 'medium' | 'large'
		reverse?: boolean
		iconRight?: boolean
		size?: 'small' | 'medium' | 'large'
		buttons?: {
			label?: string
			secondary?: boolean
			tertiary?: boolean
			disabled?: boolean
			icon?: string
			iconOnly?: boolean
			noOutline?: boolean
			// Omitted: iconRight, size
			// Custom props
			link?: string
			copy?: string
		}[]
		equisized?: boolean
	}>
>()

const clicked = ref<boolean[]>(Array(props.args.buttons?.length ?? 0).fill(false))

async function onClick(event: any)
{
	let button = event.target
	while (button && !button.classList.contains('fr-btn'))
	{
		button = button.parentElement
	}

	if (!button)
	{
		console.error('Button not found for click event:', event)
		return
	}

	// Button is located at `.component .fr-btns-group > li > .fr-btn`
	// Get the index of the button in the group
	const index = Array.from(
		button.parentElement?.parentElement?.children ?? []
	).indexOf(button.parentElement)

	const buttonArgs = props.args.buttons?.[index]

	if (buttonArgs)
	{
		if (buttonArgs.link)
		{
			window.open(buttonArgs.link, '_blank')?.focus()
		}
		else if (buttonArgs.copy)
		{
			navigator.clipboard.writeText(buttonArgs.copy)
				.catch(err =>
					{
						console.error('Failed to copy:', err)
					})
		}
	}

	if (clicked.value.some(value => value))
	{
		clicked.value = Array(props.args.buttons?.length ?? 0).fill(false)
		Streamlit.setComponentValue([...clicked.value])

		await new Promise(resolve => setTimeout(resolve, 50))
	}

	clicked.value[index] = true
	Streamlit.setComponentValue([...clicked.value])

	await new Promise(resolve => setTimeout(resolve, 50))

	clicked.value[index] = false
	Streamlit.setComponentValue([...clicked.value])
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButtonGroup
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			@click="onClick"
		/>
	</div>
</template>

<style scoped>
.component {
	/* Remove the bottom margin of the button group */
	margin-bottom: -1rem;
}
</style>
