<script setup lang="ts">
import { reactive, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrCheckbox } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		disabled?: boolean
		// Props
		modelValue?: boolean
		required?: boolean
		small?: boolean
		name?: string
		hint?: string
		id?: string
		inline?: boolean
		errorMessage?: string
		validMessage?: string
		// Slots
		label?: string
		requiredTip?: string

	}>
>()

const checked = ref<boolean>(props.args.modelValue ?? false)
const style = reactive<{ [key: string]: string }>({})

if (props.theme)
{
	style['--base'] = props.theme.base
	style['--primary-color'] = props.theme.primaryColor
	style['--background-color'] = props.theme.backgroundColor
	style['--secondary-background-color'] = props.theme.secondaryBackgroundColor
	style['--text-color'] = props.theme.textColor
	style['--font'] = props.theme.font
}

const onInput = (event: InputEvent) =>
	{
		event.stopPropagation() // Fix
		checked.value = (event.currentTarget as HTMLInputElement).checked
		Streamlit.setComponentValue(checked.value)
	}
</script>

<template>
	<div class="component" :style="style">
		<DsfrCheckbox
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="checked"
			@input="onInput"
		>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrCheckbox>
	</div>
</template>

<style scoped>
.component :deep(.fr-fieldset__element) {
	margin-bottom: 0;
	padding-left: 0;
	padding-right: 0;
}
</style>
